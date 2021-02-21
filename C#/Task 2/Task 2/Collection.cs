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

        public void Sort(int option)
        {
            PropertyInfo[] flight_props = Type.GetType("Manage_class_Flight.Flight").GetProperties();

            Coll = Coll.OrderBy(o => flight_props[option].GetValue(o, null)).ToList();
        }

        public void Add(Flight new_fl)
        {
            Coll.Add(new_fl);
            EditFlightData(new_fl.ID);
        }

        public bool Remove(int id)
        {
            for (int i = 0; i < Coll.Count; i++)
            {
                if (Coll[i].ID == id)
                {
                    Flight removable = Coll[i];
                    Coll.Remove(removable);
                    return true;
                }
            }
            return false;
        }

        public void EditFlightData(int id)
        {
            PropertyInfo[] flp = Type.GetType("Manage_class_Flight.Flight").GetProperties();
            Flight curr = Coll.Find(o => o.ID == id);

            if (curr == null)
            {
                Console.WriteLine("Such ID does not exist");
                return;
            }


            for (int i = 1; i < flp.Length; i++)
            {
                Console.Write($"Please enter value of {flp[i].Name}: ");
                if (flp[i].PropertyType == Type.GetType("System.Single"))
                    flp[i].SetValue(curr, Single.Parse(Console.ReadLine()));
                else if (flp[i].PropertyType == Type.GetType("System.DateTime"))
                    flp[i].SetValue(curr, DateTime.Parse(Console.ReadLine()));
                else
                    flp[i].SetValue(curr, Console.ReadLine());
            }
        }

        // Verification
        public void Verify()
        {
            PropertyInfo[] flp = Type.GetType(typeof(Flight).ToString()).GetProperties();

            for (int i = 0; i < Coll.Count(); ++i)
            {
                foreach (PropertyInfo pi in flp)
                {
                    var coll_obj = pi.GetValue(Coll[i]);
                    var new_obj = pi.GetValue(new Flight());
                    if (coll_obj.Equals(new_obj))
                    {
                        Remove((int)flp[0].GetValue(Coll[i]));
                        i = -1;
                        break;
                    }
                }
            }
        }
    }
}