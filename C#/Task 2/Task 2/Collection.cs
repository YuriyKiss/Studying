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

        // Setters and Getters
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

            PropertyInfo[] flight_properties = Type.GetType(typeof(Flight).ToString()).GetProperties();

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
            PropertyInfo[] flight_props = Type.GetType(typeof(Flight).ToString()).GetProperties();

            Coll = Coll.OrderBy(o => flight_props[option].GetValue(o, null)).ToList();
        }

        public void Add(Flight new_fl)
        {
            Coll.Add(new_fl);
        }

        public void EditValue(int id, PropertyInfo prop, string value)
        {
            Flight curr = Coll.Find(o => o.ID == id);

            if (prop.PropertyType == Type.GetType("System.Single"))
                prop.SetValue(curr, Single.Parse(value));
            else if (prop.PropertyType == Type.GetType("System.DateTime"))
                prop.SetValue(curr, DateTime.Parse(value));
            else
                prop.SetValue(curr, value);
        }

        public bool Remove(int id)
        {
            for (int i = 0; i < Coll.Count; i++)
                if (Coll[i].ID == id) return Coll.Remove(Coll[i]);
            return false;
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