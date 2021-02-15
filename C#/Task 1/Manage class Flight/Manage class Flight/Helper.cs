using System;
using System.IO;
using System.Reflection;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.Collections.Generic;

namespace Manage_class_Flight
{
    class Helper
    {
        /* 
         * Const/static values
         * INFO - for exceptions messaging
         * PATH - for current project directory
         */
        private const string INFO = "\n[---------------------------------------------]\n";
        private static string PATH = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName;

        public static void MenuText()
        {
            Console.WriteLine("1. Print current collection of Flights\n" +
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
                if(option < 0 || option > 7)
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

        public static Collection GetCollectionFromJson()
        {
            while (true)
            {
                try
                {
                    Console.WriteLine("Enter file name: ");
                    string path = Console.ReadLine();
                    string jsonString = File.ReadAllText(PATH + "\\" + path);

                    Console.Clear();
                    Console.WriteLine($"Current file: \"{path}\"\n");

                    List<string> errors = new List<string>();
                    Collection dat = JsonConvert.DeserializeObject<Collection>
                        (jsonString, new JsonSerializerSettings
                            {
                                Error = delegate (object sender, Newtonsoft.Json.Serialization.ErrorEventArgs args)
                                    {
                                        errors.Add(args.ErrorContext.Error.Message);
                                        args.ErrorContext.Handled = true;
                                    },
                                Converters = { new IsoDateTimeConverter() }
                            }
                        );

                    foreach(string e in errors)
                    {
                        Console.WriteLine(e);
                    }

                    if (dat == null)
                    {
                        Console.WriteLine($"{INFO}Collection is a null. Empty file?{INFO}");
                        continue;
                    }

                    return dat;
                }
                catch (FileNotFoundException)
                {
                    Console.WriteLine($"{INFO}Such file does not exist{INFO}");
                }
                catch (System.Text.Json.JsonException)
                {
                    Console.WriteLine($"{INFO}File info is not in json format{INFO}");
                }
                catch (System.IO.DirectoryNotFoundException)
                {
                    Console.WriteLine($"{INFO}Directory not found (null string){INFO}");
                }
                catch
                {
                    Console.WriteLine($"{INFO}Incorrect input{INFO}");
                }
            }
        }

        public static void WriteToFile(Collection info)
        {
            try
            {
                Console.WriteLine("File to write data to:");
                string path = Console.ReadLine();

                File.WriteAllText(PATH + "\\" + path, JsonConvert.SerializeObject(info, Formatting.Indented));
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

        public static void EditFlight(Collection obj)
        {
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
                
            if (to_edit == null)
            {
                Console.WriteLine("Flight with such ID does not exist");
                return;
            }

            PropertyInfo[] flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();
            try
            {
                for (int i = 1; i < flight_properties.Length; i++)
                {
                    Console.WriteLine($"Please enter value of {flight_properties[i].ToString()}:");
                    if (i == 5) flight_properties[i].SetValue(to_edit, Single.Parse(Console.ReadLine()));
                    else if (i == 3 || i == 4) flight_properties[i].SetValue(to_edit, DateTime.Parse(Console.ReadLine()));
                    else flight_properties[i].SetValue(to_edit, Console.ReadLine());
                }
                obj.Edit(to_edit);
            }
            catch
            {
                Console.WriteLine("\nException occured while parsing previous statement\nStart editing object from scratch\n");
            }
        }
    }
}
