using System;
using System.Linq;
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
            return context.Flights.Find(id);
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
        public int Delete(int id)
        {
            Flight to_remove = null;
            foreach (Flight x in context.Flights)
                if (x.ID == id)
                    to_remove = x;
            if (to_remove != null)
            {
                context.Flights.Remove(to_remove);
                context.SaveChanges();
                return 202;
            }
            return 404;
        }
        public int Edit(int id, Flight toEdit)
        {
            var entity = context.Flights.FirstOrDefault(item => item.ID == id);

            if (entity != null)
            {
                context.Flights.Remove(entity);
                context.Flights.Add(toEdit);
                context.SaveChanges();
                return 202;
            }
            return 404;
        }
    }
}