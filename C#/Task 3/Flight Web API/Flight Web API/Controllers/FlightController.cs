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

        
    }
}