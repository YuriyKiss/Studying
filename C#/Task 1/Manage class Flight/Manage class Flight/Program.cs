using System;

namespace Manage_class_Flight
{
    class Program
    {
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
                        Helper.SortFlight(obj);
                        break;
                    case 4:
                        Helper.AddFlight(obj);
                        obj.VerifyData();
                        break;
                    case 5:
                        Helper.EditFlight(obj);
                        break;
                    case 6:
                        Helper.DeleteFlight(obj);
                        break;
                    case 7:
                        Helper.WriteToFile(obj);
                        break;
                }
            }
        }
    }
}
