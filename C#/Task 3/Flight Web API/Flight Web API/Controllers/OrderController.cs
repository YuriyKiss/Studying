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

        public OrdersController(IOrderControllerService ser)
        {
            service = ser;
        }

        [HttpPost]
        [Authorize]
        public ActionResult CreateOrder(Order toAdd)
        {
            if (ModelState.IsValid)
            {
                if (service.Create(toAdd, User.FindFirstValue(ClaimTypes.Name)) == 201)
                    return Created("", new { status = 201, message = "Order was created successfully" });
                return BadRequest(new { status = 400, message = "Flight ID does not exist or there are none places left" });
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