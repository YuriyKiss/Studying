using System.Security.Claims;
using System.Collections.Generic;

using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;

using Flight_Web_API.Models;
using Flight_Web_API.Sevices;

namespace Flight_Web_API.Controllers
{
    [Route("api/orders/")]
    [ApiController]
    public class OrdersController : ControllerBase
    {
        private IOrderControllerService service;
        private IFlightControllerService fl;

        public OrdersController(IOrderControllerService ser, IFlightControllerService f)
        {
            service = ser;
            fl = f;
        }

        [HttpPost]
        [Authorize]
        public ActionResult CreateOrder(Order toAdd)
        {
            // Spaghetti code. Haven't figured out how to make it properly yet
            if (ModelState.IsValid)
            {
                Flight dat = fl.GetOne(toAdd.FlightID);
                if (dat == null)
                    return NotFound(new { status = 404, message = "Flight ID does not exist" });
                if(dat.Places - toAdd.Places < 0)
                    return BadRequest(new { status = 400, message = "There are not enough places" });
                if (service.Create(toAdd, User.FindFirstValue(ClaimTypes.Name)) == 201)
                {
                    dat.Places -= toAdd.Places;
                    fl.Edit(dat.ID, dat);
                    return Created("", new { status = 201, message = "Order was created successfully" });
                }
                return BadRequest(new { status = 400, message = "Exception occured" });
            }
            return BadRequest(new { status = 400, message = "POST get incorrect data" });
        }

        [HttpGet]
        [Authorize]
        public ActionResult GetOrders()
        {
            List<Order> get = service.GetOrders(User.FindFirstValue(ClaimTypes.Name));
            if (get != null)
                return Ok(new { status = 200, get });
            return NotFound(new { status = 404, message = "You never had any Orders" });
        }

        [HttpGet]
        [Authorize]
        [Route("{id}")]
        public ActionResult GetOrder(int id)
        {
            Order get = service.GetOrder(id, User.FindFirstValue(ClaimTypes.Name));
            if (get != null)
                return Ok(new { status = 200, get });
            return NotFound(new { status = 404, message = "You never had order with that ID" });
        }
    }
} 