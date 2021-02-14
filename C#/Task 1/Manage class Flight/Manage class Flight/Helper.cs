using System;
using System.IO;
using System.Text.Json;

namespace Manage_class_Flight
{
    class Helper
    {
        private const string INFO = "\n[---------------------------------------------]\n";
        private const string PATH = @"E:\Programs\GitHub Repos\Studying\C#\Task 1\Manage class Flight\Manage class Flight\";

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
                if(option < 0)
                {
                    Console.WriteLine($"{INFO}Menu option can't be lesser than 0{INFO}");
                }
                else if(option > 7)
                {
                    Console.WriteLine($"{INFO}Menu option can't be bigger than 7{INFO}");
                }
                return option;
            }
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
                    string jsonString = File.ReadAllText(PATH + path);

                    Console.Clear();
                    Console.WriteLine($"Current file: \"{path}\"\n");

                    Collection dat = JsonSerializer.Deserialize<Collection>(jsonString);
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
                catch (Exception)
                {
                    Console.WriteLine($"{INFO}Incorrect input{INFO}");
                }
            }
        }
    }
}
