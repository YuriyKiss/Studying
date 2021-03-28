using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using Flight_Web_API.Models;
using Flight_Web_API.Sevices;

namespace Flight_Web_API.Controllers
{
    [Route("api/flights/")]
    [ApiController]
    public class FlightsController : ControllerBase
    {
        private IFlightControllerService service;

        public FlightsController(IFlightControllerService ser)
        {
            service = ser;
        }

        [HttpGet]
        public ActionResult GetAll(string search, string sortBy, string sortOrder, int offset, int limit)
        {
            var (result, count) = service.GetAll(search, sortBy, sortOrder, offset, limit);
            if (count > 0)
                return Ok(new { result, count });
            return BadRequest("No orders found");
        }

        [HttpGet]
        [Route("{id}")]
        public ActionResult GetOne(int id)
        {
            Flight get = service.GetOne(id);
            if (get != null)
                return Ok(get);
            return NotFound("Flight with such ID was not found");
        }

        [HttpPost]
        public ActionResult Create(Flight toAdd)
        {
            if (ModelState.IsValid)
            {
                if(service.Create(toAdd) == 201)
                    return Created($"api/flights/{toAdd.ID}", "Flight was created successfully");
                return BadRequest("Flight ID already exist");
            }
            return BadRequest("POST get incorrect data values");
        }

        [HttpDelete]
        [Route("{id}")]
        public ActionResult Delete(int id)
        {
            if (service.Delete(id) == 202)
                return Accepted("Flight was successfully deleted");
            return NotFound("Flight with such ID was not found");
        }

        [HttpPut]
        [Route("{id}")]
        public ActionResult Edit(int id, Flight toEdit)
        {
            toEdit.ID = id;
            if (ModelState.IsValid)
            {
                if(service.Edit(id, toEdit) == 202)
                    return Accepted($"api/flights/{toEdit.ID}", "Flight was edited successfully");
                return NotFound("Flight ID does not exist");
            }
            return BadRequest("PUT get incorrect data values");
        }
    }
}