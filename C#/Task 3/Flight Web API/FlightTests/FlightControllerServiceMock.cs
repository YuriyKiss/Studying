using System;
using System.Linq;
using System.Reflection;
using System.Collections.Generic;

using Flight_Web_API.Models;
using Flight_Web_API.Sevices;

namespace FlightTests
{
    class FlightControllerServiceMock : IFlightControllerService
    {
        private readonly List<Flight> info;

        public FlightControllerServiceMock()
        {
            info = new List<Flight>()
            {
                new Flight()
                {
                    ID = 1,
                    DepartureCountry = "Ukraine",
                    ArrivalCountry = "Japan",
                    DepartureTime = new DateTime(2021, 05, 18, 6, 30, 0),
                    ArrivalTime = new DateTime(2021, 05, 18, 8, 0, 0),
                    TicketPrice = 1300,
                    CompanyName = "Ryanair"
                },
                new Flight()
                {
                    ID = 2,
                    DepartureCountry = "France",
                    ArrivalCountry = "USA",
                    DepartureTime = new DateTime(2021, 06, 21, 16, 0, 0),
                    ArrivalTime = new DateTime(2021, 06, 21, 17, 0, 0),
                    TicketPrice = 2200,
                    CompanyName = "ANA"
                },
                new Flight()
                {
                    ID = 3,
                    DepartureCountry = "England",
                    ArrivalCountry = "Italy",
                    DepartureTime = new DateTime(2021, 07, 22, 12, 0, 0),
                    ArrivalTime = new DateTime(2021, 07, 22, 13, 20, 0),
                    TicketPrice = 400,
                    CompanyName = "EVA"
                },
                new Flight()
                {
                    ID = 4,
                    DepartureCountry = "France",
                    ArrivalCountry = "Japan",
                    DepartureTime = new DateTime(2021, 07, 12, 11, 20, 0),
                    ArrivalTime = new DateTime(2021, 07, 12, 12, 35, 0),
                    TicketPrice = 870,
                    CompanyName = "Ryanair"
                },
                new Flight()
                {
                    ID = 5,
                    DepartureCountry = "England",
                    ArrivalCountry = "USA",
                    DepartureTime = new DateTime(2021, 08, 10, 13, 45, 0),
                    ArrivalTime = new DateTime(2021, 08, 10, 14, 50, 0),
                    TicketPrice = 870,
                    CompanyName = "Ryanair"
                }
            };
        }

        public int Create(Flight toAdd)
        {
            foreach (Flight x in info)
                if (x.ID == toAdd.ID)
                    return 404;
            try { info.Add(toAdd); }
            catch { return 404; }
            return 201;
        }

        public int Delete(int id)
        {
            Flight to_remove = null;
            foreach (Flight x in info)
                if (x.ID == id)
                    to_remove = x;
            if (to_remove != null)
            {
                info.Remove(to_remove);
                return 202;
            }
            return 404;
        }

        public int Edit(int id, Flight toEdit)
        {
            var entity = info.FirstOrDefault(item => item.ID == id);

            if (entity != null)
            {
                foreach (var prop in toEdit.GetType().GetProperties())
                {
                    try { prop.SetValue(entity, prop.GetValue(toEdit)); }
                    catch { return 401; }
                }
                return 202;
            }
            return 404;
        }

        public (List<Flight> result, int count) GetAll(string search, string sortBy, string sortOrder, int offset, int limit)
        {
            List<Flight> data = info;

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
                if (sortOrder == "desc")
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
            return info.Find(o => o.ID == id);
        }
    }
}
