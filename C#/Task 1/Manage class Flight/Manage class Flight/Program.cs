using System;
using System.Reflection;

namespace Manage_class_Flight
{
    class Program
    {
        private const string INFO = Helper.INFO;

        static void Main()
        {
            Collection obj = Helper.GetCollectionFromJson();
            obj.VerifyData();

            bool flag = true;
            while (flag)
            {
                Helper.MenuText();
                int option = Helper.GetMenuOption();
                switch (option)
                {
                    default:
                        break;
                    case 0:
                        flag = false;   
                        break;
                    case 1:
                        Console.Clear();
                        Console.WriteLine(obj);
                        break;
                    case 2:
                        Console.Clear();
                        Console.WriteLine("Enter search term: ");
                        Console.WriteLine(obj.Search(Console.ReadLine()));
                        break;
                    case 3:
                        SortFlight(obj);
                        break;
                    case 4:
                        AddFlight(obj);
                        obj.VerifyData();
                        break;
                    case 5:
                        EditFlight(obj);
                        break;
                    case 6:
                        DeleteFlight(obj);
                        break;
                    case 7:
                        Helper.WriteToFile(obj);
                        break;
                }
            }
        }

        public static void AddFlight(Collection obj)
        {
            Console.Clear();
            PropertyInfo[] flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();
            Flight new_fl = new Flight();

            obj.Sort(flight_properties, 0);
            flight_properties[0].SetValue(new_fl, obj.Coll[^1].ID + 1);
            try
            {
                EditFlightData(flight_properties, new_fl);
                obj.Coll.Add(new_fl);
            }
            catch
            {
                Console.WriteLine("\nException occured while parsing previous statement\nStart creating\\editing object from scratch\n");
                return;
            }
        }

        public static void EditFlight(Collection obj)
        {
            Console.Clear();
            Console.WriteLine(obj);
            Console.WriteLine("Choose flight ID to edit: ");

            Flight to_edit = new Flight();
            try
            {
                int id = Int32.Parse(Console.ReadLine());
                foreach (Flight f in obj.Coll)
                {
                    if (f.ID == id) to_edit = f;
                }
            }
            catch
            { Console.WriteLine("Error occured while parsing ID"); }

            if (to_edit.ID == new Flight().ID)
            {
                Console.WriteLine($"{INFO}Flight with such ID does not exist{INFO}");
                return;
            }

            Flight save = (Flight)to_edit.DeepCopy();
            PropertyInfo[] flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();
            try
            {
                EditFlightData(flight_properties, to_edit);
                if (!to_edit.Verify())
                    obj.Edit(save);
            }
            catch
            {
                obj.Edit(save);
                Console.WriteLine("\nException occured while parsing previous statement\nStart editing object from scratch\n");
                return;
            }
        }

        public static void EditFlightData(PropertyInfo[] flp, Flight new_fl)
        {
            for (int i = 1; i < flp.Length; i++)
            {
                Console.WriteLine($"Please enter value of {flp[i].ToString()}:");
                if (flp[i].PropertyType == Type.GetType("System.Single")) flp[i].SetValue(new_fl, Single.Parse(Console.ReadLine()));
                else if (flp[i].PropertyType == Type.GetType("System.DateTime")) flp[i].SetValue(new_fl, DateTime.Parse(Console.ReadLine()));
                else flp[i].SetValue(new_fl, Console.ReadLine());
            }
        }

        public static void DeleteFlight(Collection obj)
        {
            Console.Clear();
            Console.WriteLine(obj);
            Console.WriteLine("Choose flight ID to delete: ");
            try
            {
                string id = Console.ReadLine();
                for (int i = 0; i < obj.Coll.Count; i++)
                {
                    if (obj.Coll[i].ID == Int32.Parse(id))
                    {
                        Flight removable = obj.Coll[i];
                        obj.Coll.Remove(removable);
                        return;
                    }
                }
                Console.WriteLine($"{INFO}Object with such ID does not exist{INFO}");
            }
            catch
            {
                Console.WriteLine($"{INFO}Could not parse an ID{INFO}");
            }
        }

        public static void SortFlight(Collection obj)
        {
            PropertyInfo[] flight_properties;
            flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();

            Console.Clear();
            Console.WriteLine("Choose an option to sort by: ");
            for (int i = 0; i < flight_properties.Length; i++)
            {
                Console.WriteLine($"{i}. {flight_properties[i].ToString()}");
            }
            try
            {
                int option = Int32.Parse(Console.ReadLine());
                obj.Sort(flight_properties, option);
            }
            catch { Console.WriteLine($"{INFO}Input is a single number, not a string, char or null\nTry sorting again{INFO}"); }
        }
    }
}
