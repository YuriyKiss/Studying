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
        public void Delete(string id)
        {
            try
            {
                Flight to_delete = new Flight();
                foreach(Flight f in Coll)
                {
                    if (f.ID == Int32.Parse(id)) to_delete = f;
                }
                if (!Coll.Remove(to_delete))
                {
                    Console.WriteLine("ID was not found in collection\n");
                }
            }
            catch
            {
                Console.WriteLine("Unresolved exception occured, while deleting ID\n");
            }
        }

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
                        response += $"Flight ID - {f.ID} contains \"{request}\" in {flight_properties[i]}\n";
                    }
                }
            }

            return response;
        }

        public void Sort()
        {
            PropertyInfo[] flight_properties;
            flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();

            Console.WriteLine("Choose an option to sort by: ");
            for (int i = 0; i < flight_properties.Length; i++)
            {
                Console.WriteLine($"{i}. {flight_properties[i].ToString()}");
            }
            try
            {
                int option = Int32.Parse(Console.ReadLine());
                Coll = Coll.OrderBy(o => flight_properties[option].GetValue(o, null)).ToList();
            }
            catch { Console.WriteLine("Input is a single number, not a string or char. Try sorting again\n"); }
        }

        public void Add()
        {
            PropertyInfo[] flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();

            Flight new_fl = new Flight();
            Console.WriteLine("Creating new Flight...");
            try
            {
                for (int i = 0; i < flight_properties.Length; i++)
                {
                    Console.WriteLine($"Please enter value of {flight_properties[i].ToString()}:");
                    if (i == 0) flight_properties[i].SetValue(new_fl, Int32.Parse(Console.ReadLine()));
                    else if (i == 5) flight_properties[i].SetValue(new_fl, Single.Parse(Console.ReadLine()));
                    else if (i == 3 || i == 4) flight_properties[i].SetValue(new_fl, DateTime.Parse(Console.ReadLine()));
                    else flight_properties[i].SetValue(new_fl, Console.ReadLine());
                }
                Coll.Add(new_fl);
            }
            catch { Console.WriteLine("\nException occured while parsing previous statement\nStart creating object from scratch\n"); }  
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
