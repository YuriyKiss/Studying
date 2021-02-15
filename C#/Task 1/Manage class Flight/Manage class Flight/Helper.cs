using System;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.Collections.Generic;

namespace Manage_class_Flight
{
    class Helper
    {
        public const string INFO = "\n[---------------------------------------------]\n";
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

        public static void WriteToFile(Collection info)
        {
            try
            {
                Console.Clear();
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
    }
}