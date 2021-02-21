using System;
using System.Linq;
using System.Reflection;
using System.Collections.Generic;

namespace Manage_class_Flight
{
    class Collection<T>
    {
        // Constructors
        public Collection()
        {
            Coll = new List<T>();
        }

        public Collection(List<T> data)
        {
            Coll = data;
        }

        // Setters and Getters
        public List<T> Coll { get; set; }

        // Functions override
        public override string ToString()
        {
            string resp = "";
            foreach (T a in Coll)
            {
                resp += a.ToString() + "\n";
            }
            return resp;
        }

        // Functionality
        public string Search(string request)
        {
            string response = "";

            PropertyInfo[] properties = Type.GetType(typeof(T).ToString()).GetProperties();

            foreach (T t in Coll)
            {
                for (int i = 0; i < properties.Length; i++)
                {
                    if (properties[i].GetValue(t).ToString().ToLower().Contains(request.ToLower()))
                    {
                        response += $"Object with ID {properties[0].GetValue(t)} contains \"{request}\" in {properties[i].Name}\n";
                    }
                }
            }

            return response;
        }

        public void Sort(int option)
        {
            PropertyInfo[] props = Type.GetType(typeof(T).ToString()).GetProperties();

            Coll = Coll.OrderBy(o => props[option].GetValue(o, null)).ToList();
        }

        public void Add(T new_obj)
        {
            Coll.Add(new_obj);
        }

        public void EditValue(int id, PropertyInfo prop, string value)
        {
            T curr = Coll.Find(o => (int)this.GetType().GetProperties()[0].GetValue(o) == id);

            // Definitely needs more Type parsers when in use with other's classes (Int32, Duoble, (?))
            if (prop.PropertyType == Type.GetType("System.Single"))
                prop.SetValue(curr, Single.Parse(value));
            else if (prop.PropertyType == Type.GetType("System.DateTime"))
                prop.SetValue(curr, DateTime.Parse(value));
            else if (prop.PropertyType == Type.GetType("System.Double"))
                prop.SetValue(curr, Double.Parse(value));
            else
                prop.SetValue(curr, value);
        }

        public bool Remove(int id)
        {
            for (int i = 0; i < Coll.Count; i++)
                if ((int)this.GetType().GetProperties()[0].GetValue(Coll[i]) == id) return Coll.Remove(Coll[i]);
            return false;
        }

        // Verification
        public void Verify()
        {
            PropertyInfo[] props = Type.GetType(typeof(T).ToString()).GetProperties();

            for (int i = 0; i < Coll.Count(); ++i)
            {
                foreach (PropertyInfo pi in props)
                {
                    var coll_obj = pi.GetValue(Coll[i]);
                    if (coll_obj.Equals(0) || coll_obj.Equals(null) || coll_obj.Equals(new DateTime()))
                    {
                        Remove((int)props[0].GetValue(Coll[i]));
                        i = -1;
                        break;
                    }
                }
            }
        }
    }
}