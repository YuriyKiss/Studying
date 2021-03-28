using System;
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

        public (List<Flight> result, int count) GetAll(string search, string sortBy, string sortOrder, int offset, int limit)
        {
            throw new NotImplementedException();
        }
        public Flight GetOne(int id)
        {
            throw new NotImplementedException();
        }

        public int Create(Flight toAdd)
        {
            try
            {
                context.Flights.Add(toAdd);
                context.SaveChanges();
            }
            catch { return 404; }
            return 201;
        }
        public Flight Delete(int id)
        {
            throw new NotImplementedException();
        }
        public int Edit(int id, Flight toEdit)
        {
            throw new NotImplementedException();
        }
    }
}