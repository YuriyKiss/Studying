using Microsoft.AspNetCore.Mvc;

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

        /// <summary>
        /// Get all Flights | Apply Search | Sort Parameter | Sort Order | Offset | Limit on one page
        /// </summary>
        /// <param name="search">Func will only return flights that contain "search" substring in any attribute</param>
        /// <param name="sortBy" example="TicketPrice">Func will return flights sorted by given attribute</param>
        /// <param name="sortOrder" example="'desc' OR 'asc'">Func will return flights in given order. If sortBy is not defined - sorts by ID</param>
        /// <param name="offset">Which page we choose? (if null offset = 1)</param>
        /// <param name="limit">How much flights on one page (if null limit = all flights)</param>
        /// <returns>A list of flights that coresponds to given parameters</returns>
        /// <response code="200">Returns list of coresponding flights</response>
        /// <response code="404">If the item is null</response>  
        [HttpGet]
        public ActionResult GetAll(string search, string sortBy, string sortOrder, int offset, int limit)
        {
            var (result, count) = service.GetAll(search, sortBy, sortOrder, offset, limit);
            if (count > 0)
                return Ok(new { result, count });
            return NotFound("No orders found");
        }

        /// <summary>
        /// Finds a Flight by given ID
        /// </summary>
        /// <param name="id">ID to search in DB</param>
        /// <returns>Found Flight</returns>
        /// <response code="200">Returns found Flight</response>
        /// <response code="404">If Flight is null</response>  
        [HttpGet]
        [Route("{id}")]
        public ActionResult GetOne(int id)
        {
            Flight get = service.GetOne(id);
            if (get != null)
                return Ok(get);
            return NotFound("Flight with such ID was not found");
        }

        /// <summary>
        /// Creates given Flight and Inserts it into DB
        /// </summary>
        /// <remarks>
        /// Sample request:
        ///
        ///     POST 
        ///     {
        ///        "ID": 3,
        ///        "DepartureCountry": "Ukraine",
        ///        "ArrivalCountry": "Japan",
        ///        "DepartureTime": "2021-06-16T21:30",
        ///        "ArrivalTime": "2021-06-16T23:45",
        ///        "TicketPrice": 1500,
        ///        "CompanyName": "Wizzair"
        ///     }
        ///
        /// </remarks>
        /// <returns>Success Message and Link to GET Flight</returns>
        /// <response code="201">Returns Success Message</response>
        /// <response code="400">If Flight data is not valid OR ID is taken</response>
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

        /// <summary>
        /// Deletes Flight with ID
        /// </summary>
        /// <param name="id">ID of Flight to delete</param>
        /// <returns>Success Message</returns>
        /// <response code="202">Returns Success Message</response>
        /// <response code="404">If Flight with ID does not exist</response>  
        [HttpDelete]
        [Route("{id}")]
        public ActionResult Delete(int id)
        {
            if (service.Delete(id) == 202)
                return Accepted("Flight was successfully deleted");
            return NotFound("Flight with such ID was not found");
        }

        /// <summary>
        /// Edits a Flight with parameters from PUT request
        /// </summary>
        /// <remarks>
        /// Sample request:
        ///
        ///     PUT /1
        ///     {
        ///        "DepartureCountry": "Ukraine",
        ///        "ArrivalCountry": "France",
        ///        "DepartureTime": "2021-06-16T21:30",
        ///        "ArrivalTime": "2021-06-16T23:45",
        ///        "TicketPrice": 1250,
        ///        "CompanyName": "ANA"
        ///     }
        ///
        /// </remarks>
        /// <param name="id">ID of Flight to edit</param>
        /// <param name="toEdit">New Data for Flight</param>
        /// <returns>Success Message and Link to GET Flight</returns>
        /// <response code="202">Returns Success Message</response>
        /// <response code="400">If Flight data is not valid</response>
        /// <response code="404">If Fligth with such ID does not exist</response>
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