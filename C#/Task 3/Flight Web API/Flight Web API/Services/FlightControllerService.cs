using System.Linq;
using System.Reflection;
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
            List<Flight> data = context.Flights.ToList<Flight>();

            if (search != null)
                foreach (Flight flight in data.ToList())
                    foreach (PropertyInfo prop in typeof(Flight).GetProperties())
                    {
                        if (prop.GetValue(flight).ToString().ToLower().Contains(search.ToLower()))
                            break;
                        if (prop.Name == typeof(Flight).GetProperties().Last().Name) data.Remove(flight);
                    }

            foreach (PropertyInfo prop in typeof(Flight).GetProperties())
            {
                if (prop.Name == sortBy) break;
                if (prop.Name == typeof(Flight).GetProperties().Last().Name) sortBy = null;
            }

            if (sortBy != null)
            {
                if(sortOrder == "desc")
                    data = data.OrderByDescending(o => typeof(Flight).GetProperty(sortBy).GetValue(o)).ToList();
                else
                    data = data.OrderBy(o => typeof(Flight).GetProperty(sortBy).GetValue(o)).ToList();
            }
            else 
            {
                if (sortOrder == "desc")
                    data = data.OrderByDescending(o => o.ID).ToList();
                else
                    data = data.OrderBy(o => o.ID).ToList();
            }

            if (limit == null || limit < 1) limit = data.Count;
            if (offset == null || offset < 1) offset = 1;
            data = data.Skip(limit * (offset - 1)).Take(limit).ToList();

            return (data, data.Count);
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
                foreach (var prop in toEdit.GetType().GetProperties())
                {
                    try { prop.SetValue(entity, prop.GetValue(toEdit)); }
                    catch { return 401; }
                }

                context.Flights.Update(entity);
                context.SaveChanges();
                return 202;
            }
            return 404;
        }
    }
}