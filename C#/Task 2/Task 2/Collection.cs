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

        public void EditValue(Guid id, PropertyInfo prop, string value)
        {
            T curr = Coll.Find(o => (Guid)Type.GetType(typeof(T).ToString()).GetProperties()[0].GetValue(o) == id);

            var converted_value = Convert.ChangeType(value, prop.PropertyType);

            prop.SetValue(curr, converted_value);
        }

        public bool Remove(Guid id)
        {
            for (int i = 0; i < Coll.Count; i++)
                if ((Guid)Type.GetType(typeof(T).ToString()).GetProperties()[0].GetValue(Coll[i]) == id) 
                    return Coll.Remove(Coll[i]);
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
                        Remove((Guid)props[0].GetValue(Coll[i]));
                        i = -1;
                        break;
                    }
                }
            }
        }

    }
}