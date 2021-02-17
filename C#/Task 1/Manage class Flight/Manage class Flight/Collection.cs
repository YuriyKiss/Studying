using System;
using System.Linq;
using System.Reflection;
using System.Collections.Generic;

namespace Manage_class_Flight
{
    class Collection
    {
        // Constructors
        public Collection()
        {
            Coll = new List<Flight>();
        }

        public Collection(List<Flight> data)
        {
            Coll = data;
        }

        // Properties
        public List<Flight> Coll { get; set; }

        // Functions override
        public override string ToString()
        {
            string resp = "";
            foreach (Flight a in Coll)
            {
                resp += a.ToString() + "\n";
            }
            return resp;
        }

        // Integrity check
        public void VerifyData()
        {
            List<Flight> delete_later = new List<Flight>();
            foreach(Flight f in Coll)
            {
                if (!f.Verify())
                {
                    delete_later.Add(f);
                }
            }
            foreach(Flight f in delete_later)
            {
                Coll.Remove(f);
            }
        }

        // Functionality
        public string Search(string request)
        {
            string response = "";

            PropertyInfo[] flight_properties;
            flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();

            foreach (Flight f in Coll)
            {
                for (int i = 0; i < flight_properties.Length; i++)
                {
                    if (flight_properties[i].GetValue(f).ToString().ToLower().Contains(request.ToLower()))
                    {
                        response += $"Flight with ID {f.ID} contains \"{request}\" in {flight_properties[i].Name}\n";
                    }
                }
            }

            return response;
        }

        public void Sort(PropertyInfo[] flight_props, int option)
        {
            Coll = Coll.OrderBy(o => flight_props[option].GetValue(o, null)).ToList();
        }

        public void Edit(Flight right)
        {
            for (int i = 0; i < Coll.Count(); i++)
            {
                if (Coll[i].ID == right.ID) Coll[i] = right;
            }
        }
    }
}