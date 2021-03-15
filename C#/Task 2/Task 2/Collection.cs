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
            Verify();
        }

        public void EditValue(int id, PropertyInfo prop, string value)
        {
            PropertyInfo pi = typeof(T).GetProperty("ID");

            T obj = Coll.Find(o => (int)pi.GetValue(o) == id);

            var converted_value = Convert.ChangeType(value, prop.PropertyType);

            prop.SetValue(obj, converted_value);
        }

        public bool Remove(string id)
        {
            PropertyInfo pi = typeof(T).GetProperty("ID");

            T obj = Coll.Find(o => pi.GetValue(o).ToString() == id);

            return Coll.Remove(obj);
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
                        T removable = Coll.Find(o => pi.GetValue(o).ToString() == pi.GetValue(Coll[i]).ToString());
                        Coll.Remove(removable);
                        i = -1;
                        break;
                    }
                }
            }
        }
    }
}