using System;
using System.Linq;
using System.IdentityModel.Tokens.Jwt;

using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;

using Flight_Web_API.Models;
using Flight_Web_API.Sevices;

namespace Flight_Web_API.Controllers
{
    [Route("api/users/")]
    [ApiController]
    public class UsersController : ControllerBase
    {
        private IUserControllerService service;

        public UsersController(IUserControllerService ser)
        {
            service = ser;
        }

        /// <summary>
        /// Registers user and saves him in DB
        /// </summary>
        /// <remarks>
        /// Sample request:
        ///
        ///     POST 
        ///     {
        ///        "Login": "username",
        ///        "Password": "username"
        ///     }
        ///
        /// </remarks>
        /// <returns>Success Message</returns>
        /// <response code="201">Returns Success Message</response>
        /// <response code="400">If User login or pass is not valid</response>
        [HttpPost]
        public ActionResult Register(User toAdd)
        {
            if (ModelState.IsValid)
            {
                if (service.Register(toAdd) == 201)
                    return Created($"username = {toAdd.Login}", new { status = 201, message = "User was registered successfully" });
                return BadRequest(new { status = 400, message = "User login is already taken" });
            }
            return BadRequest(new { status = 400, message = "POST get incorrect data" });
        }

        [HttpGet]
        public ActionResult Login(User loggging_in)
        {
            if (ModelState.IsValid)
            { 
                var identity = service.FindUser(loggging_in.Login, loggging_in.Password);
                if (identity == null)
                {
                    return NotFound(new { status = 404, errorText = "Invalid username or password." });
                }

                var now = DateTime.UtcNow;

                var jwt = new JwtSecurityToken(
                        issuer: AuthOptions.ISSUER,
                        audience: AuthOptions.AUDIENCE,
                        notBefore: now,
                        claims: identity.Claims,
                        expires: now.Add(TimeSpan.FromMinutes(AuthOptions.LIFETIME)),
                        signingCredentials: new SigningCredentials(AuthOptions.GetSymmetricSecurityKey(), SecurityAlgorithms.HmacSha256));

                var encodedJwt = new JwtSecurityTokenHandler().WriteToken(jwt);

                return Ok(new { status = 200, access_token = encodedJwt, username = identity.Name, role = (identity.Claims.ToList())[1].Value });
            }
            return BadRequest(new { status = 400, message = "Model of User is incorrect" });
        }
    }
}