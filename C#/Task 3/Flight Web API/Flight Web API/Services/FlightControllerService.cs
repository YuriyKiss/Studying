using System.Collections.Generic;
using Flight_Web_API.Models;

namespace Flight_Web_API.Sevices
{
    public class  FlightControllerService : IFlightControllerService
    {
        private FlightsContext context = new FlightsContext();

        public FlightControllerService(FlightsContext cont)
        {
            context = cont;
        }

        public (List<Flight> res, int count) GetAll(string search, string sortBy, string sortOrder, int offset, int limit);
        public Flight GetOne(int id);

        public int Create(Flight toAdd);
        public Flight Delete(int id);
        public int Edit(int id, Flight toEdit);
    }
}