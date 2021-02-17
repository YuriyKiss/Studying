﻿using System;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.Collections.Generic;
using System.Reflection;

namespace Manage_class_Flight
{
    class Program
    {
        private const string INFO = "\n[---------------------------------------------]\n";
        private static string PATH = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName;
        private static Collection obj = GetCollectionFromJson();
        
        static void Main()
        {
            obj.VerifyData();

            bool flag = true;
            while (flag)
            {
                MenuText();
                int option = GetMenuOption();
                switch (option)
                {
                    default:
                        break;
                    case 0:
                        flag = false;   
                        break;
                    case 1: Print();
                        break;
                    case 2: Search();
                        break;
                    case 3: Sort();
                        break;
                    case 4:
                        AddFlight();
                        obj.VerifyData();
                        break;
                    case 5:
                        EditFlight();
                        break;
                    case 6:
                        DeleteFlight();
                        break;
                    case 7:
                        WriteToFile();
                        break;
                }
            }
        }

        public static Collection GetCollectionFromJson()
        {
            while (true)
            {
                try
                {
                    Console.Write("Enter file name: ");
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

                    foreach (string e in errors)
                    {
                        Console.WriteLine(e);
                    }

                    if (dat == null)
                    {
                        Console.WriteLine($"{INFO}Collection is a null. Empty file or incorrect format{INFO}");
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

        public static void Print()
        {
            Console.Clear();
            Console.Write(obj);
        }

        public static void Search()
        {
            Console.Clear();
            Console.Write("Enter search term: ");

            string search_request = Console.ReadLine();
            string collection_respond = obj.Search(search_request);

            Console.Write("\n" + collection_respond + "\n");
        }

        public static void Sort()
        {
            Console.Clear();
            
            PropertyInfo[] flight_properties = Type.GetType("Manage_class_Flight.Flight").GetProperties();
            for (int i = 0; i < flight_properties.Length; i++)
            {
                Console.WriteLine($"{i}. {flight_properties[i].Name}");
            }

            Console.Write("\nChoose an option to sort by: ");
            try
            {
                int option = Int32.Parse(Console.ReadLine());
                obj.Sort(flight_properties, option);

                Console.Clear();
                Console.WriteLine($"Successfully sorted by \"{flight_properties[option].Name}\"\n");
            }
            catch { Console.Write($"{INFO}Input is a single number, not a string, char or null\nChoose sorting option again{INFO}"); }
        }

        public static void MenuText()
        {
            Console.Write("1. Print current collection of Flights\n" +
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

        public static void WriteToFile()
        {
            try
            {
                Console.Clear();
                Console.WriteLine("File to write data to:");
                string path = Console.ReadLine();

                File.WriteAllText(PATH + "\\" + path, JsonConvert.SerializeObject(obj, Formatting.Indented));
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

        public static void AddFlight()
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
                Console.WriteLine("\nException occured while parsing previous statement\n" +
                    "Start creating\\editing object from scratch\n");
                return;
            }
        }

        public static void EditFlight()
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

        public static void DeleteFlight()
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

        

    }
}