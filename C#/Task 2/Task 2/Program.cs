using System;
using System.IO;
using Newtonsoft.Json;
using System.Reflection;
using Newtonsoft.Json.Converters;

namespace Manage_class_Flight
{
    class Program
    {
        private const string INFO = "\n[---------------------------------------------]\n";
        private static readonly string PATH = Directory.GetParent(Directory.
            GetCurrentDirectory()).Parent.Parent.FullName;
        private static Collection<Flight> obj_collection;
        
        static void Main()
        {
            obj_collection = GetCollectionFromJson<Flight>();

            bool flag = true;
            while (flag)
            {
                MenuText();
                int option = GetMenuOption();
                switch (option)
                {
                    default:
                        break;
                    case 0: flag = false;   
                        break;
                    case 1: Print();
                        break;
                    case 2: Search();
                        break;
                    case 3: Sort<Flight>();
                        break;
                    case 4: Add<Flight>();
                        break;
                    case 5: Edit<Flight>();
                        break;
                    case 6: Delete();
                        break;
                    case 7: WriteToFile();
                        break;
                }
            }
        }

        public static Collection<Flight> GetCollectionFromJson<T>()
        {
            while (true)
            {
                Console.Write("Enter file name: ");
                string path = Console.ReadLine();
                try
                {
                    string jsonString = File.ReadAllText(PATH + "\\" + path);
                
                    Console.Clear();
                    Console.WriteLine($"Current file: \"{path}\"\n");

                    Collection<Flight> dat = JsonConvert.DeserializeObject<Collection<Flight>>
                        (jsonString, new JsonSerializerSettings
                        {
                            Error = delegate (object sender, Newtonsoft.Json.Serialization.ErrorEventArgs args)
                            {
                                Console.WriteLine(args.ErrorContext.Error.Message);
                                
                                args.ErrorContext.Handled = true;
                            },
                            Converters = { new IsoDateTimeConverter() }
                        }
                        );

                    dat.Verify();
                    if (dat == null)
                    {
                        Console.Write($"{INFO}Collection is a null - file is empty or not in correct format{INFO}");
                        continue;
                    }

                    return dat;
                }
                catch
                {
                    Console.Write($"{INFO}File does not exist, is empty or contains incorrect data format{INFO}");
                }
            }
        }

        public static void MenuText()
        {
            Console.Write("1. Print current collection of Objects\n" +
                          "2. Search the collection for an element\n" +
                          "3. Sort the collection by attribute\n" +
                          "4. Add an element to a collection\n" +
                          "5. Change an element by ID\n" +
                          "6. Delete an element by ID\n" +
                          "7. Save current collection to file\n\n" +
                          "0. Exit\n" +
                          "\nPick an option: ");
        }

        public static int GetMenuOption()
        {
            try
            {
                int option = Int32.Parse(Console.ReadLine());
                if (option < 0 || option > 7)
                {
                    Console.Clear();
                    Console.WriteLine($"{INFO}Menu option can't be (lesser than 0)/(bigger than 7){INFO}");
                }
                return option;
            }
            // Yes, I decided to manage every exception separately. Easily changeable to >> catch (Exception) { //code }
            catch (FormatException)
            {
                Console.WriteLine($"{INFO}Menu option is a number, not a char or string{INFO}");
                return -1;
            }
            catch (OverflowException)
            {
                Console.WriteLine($"{INFO}Congrats, you found it. Menu option can't be THAT big or THAT small, whatever{INFO}");
                return -1;
            }
            catch (ArgumentNullException)
            {
                Console.WriteLine($"{INFO}Whole new another level of exceptions are checking we, right?\nMenu option can't be null{INFO}");
                return -1;
            }
            catch (ArgumentException)
            {
                Console.WriteLine($"{INFO}I have no idea how to get this exception, but.. it is there. In the documentation{INFO}");
                return -1;
            }
        }

        public static void Print()
        {
            Console.Clear();
            Console.Write(obj_collection);
        }

        public static void Search()
        {
            Console.Clear();
            Console.Write("Enter search term: ");

            string search_request = Console.ReadLine();
            string collection_respond = obj_collection.Search(search_request);

            Console.Write("\n" + collection_respond + "\n");
        }

        public static void Sort<T>()
        {
            Console.Clear();

            PropertyInfo[] properties = Type.GetType(typeof(T).ToString()).GetProperties();
            for (int i = 0; i < properties.Length; i++)
            {
                Console.WriteLine($"{i}. {properties[i].Name}");
            }

            Console.Write("\nChoose an option to sort by: ");
            try
            {
                int option = Int32.Parse(Console.ReadLine());
                obj_collection.Sort(option);

                Console.Clear();
                Console.WriteLine($"Successfully sorted by \"{properties[option].Name}\"\n");
            }
            catch { Console.Write($"{INFO}Input is a single number, not a string, char or null\nChoose sorting option again{INFO}"); }
        }

        public static void Add<T>() where T : Flight
        {
            T new_obj = default(T);

            obj_collection.Sort(0);

            PropertyInfo[] props = Type.GetType(typeof(T).ToString()).GetProperties();
            props[0].SetValue(new_obj, obj_collection.Coll[^1].ID + 1);

            Console.Clear();
            try
            {
                for (int i = 1; i < props.Length; i++)
                {
                    Console.Write($"Please enter value of {props[i].Name}: ");
                    if (props[i].PropertyType == Type.GetType("System.Single"))
                        props[i].SetValue(new_obj, Single.Parse(Console.ReadLine()));
                    else if (props[i].PropertyType == Type.GetType("System.DateTime"))
                        props[i].SetValue(new_obj, DateTime.Parse(Console.ReadLine()));
                    else
                        props[i].SetValue(new_obj, Console.ReadLine());
                }

                obj_collection.Add(new_obj);
            }
            catch
            {
                obj_collection.Remove(new_obj.ID);

                Console.WriteLine("\nException occured while parsing previous statement\n" +
                    "Start creating object from scratch\n");
                return;
            }
        }

        public static void Edit<T>()
        {
            try
            {
                Console.Clear();
                Console.WriteLine(obj_collection);
                Console.Write("Choose object ID to edit its property: ");

                int id = Int32.Parse(Console.ReadLine());
                if(obj_collection.Coll.Find(o => o.ID == id) == null) { throw new Exception(); }

                PropertyInfo[] props = Type.GetType(typeof(T).ToString()).GetProperties();
                for (int i = 1; i < props.Length; i++)
                {
                    Console.WriteLine($"{i}. {props[i].Name}");
                }
                Console.Write("Choose object's property to edit: ");

                PropertyInfo prop = props[Int32.Parse(Console.ReadLine())];

                Console.Write($"Enter new property value ({prop.PropertyType}) : ");
                string value = Console.ReadLine();

                obj_collection.EditValue(id, prop, value);
            }
            catch
            {
                Console.WriteLine("\nException occured while parsing previous statement\n" +
                "Start editing object from scratch\n");
            }
        }

        public static void Delete()
        {
            Console.Clear();
            Console.WriteLine(obj_collection);
            Console.Write("Choose object's ID to delete: ");

            try
            {
                int id = Int32.Parse(Console.ReadLine());
                if (obj_collection.Remove(id))
                {
                    Console.WriteLine($"Object with ID {id} removed successfully\n");
                    return;
                }
                Console.WriteLine($"{INFO}Object with such ID does not exist{INFO}");
            }
            catch
            {
                Console.WriteLine($"{INFO}Could not parse an ID{INFO}");
            }
        }

        public static void WriteToFile()
        {
            try
            {
                Console.Clear();
                Console.WriteLine("File to write data to:");
                string path = Console.ReadLine();

                File.WriteAllText(PATH + "\\" + path, JsonConvert.SerializeObject(obj_collection, Formatting.Indented));
                Console.WriteLine($"Successfully saved information to {path}\n");
            }
            catch (FileNotFoundException)
            {
                Console.WriteLine($"{INFO}Such file does not exist{INFO}");
            }
            catch
            {
                Console.WriteLine($"{INFO}Unknown exception while writing file occured{INFO}");
            }
        }
    }
}