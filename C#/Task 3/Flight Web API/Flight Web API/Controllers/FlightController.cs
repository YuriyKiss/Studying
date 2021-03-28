using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Flight_Web_API.Models;
using Flight_Web_API.Sevices;

namespace Flight_Web_API.Controllers
{
    [Route("api/flights")]
    [ApiController]
    public class FlightsController : ControllerBase
    {
        private IFlightControllerService service;

        public FlightsController(IFlightControllerService ser)
        {
            service = ser;
        }

        [HttpPost]
        public ActionResult Create(Flight toAdd)
        {
            if (ModelState.IsValid)
            {
                if(service.Create(toAdd) == 201)
                {
                    return Ok("Flight was created successfully");
                }
                return BadRequest("Flight ID already exist, or validation didn't pass");
            }
            return BadRequest("POST get incorrect data values");
        }
    }
}