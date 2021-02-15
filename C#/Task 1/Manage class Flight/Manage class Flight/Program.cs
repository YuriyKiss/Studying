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
                        Console.Clear();
                        obj.Sort();
                        break;
                    case 4:
                        Console.Clear();
                        obj.Add();
                        obj.VerifyData();
                        break;
                    case 5:
                        Console.Clear();
                        Console.WriteLine(obj);
                        Console.WriteLine("Choose flight ID to edit: ");
                        break;
                    case 6:
                        Console.Clear();
                        Console.WriteLine(obj);
                        Console.WriteLine("Choose flight ID to delete: ");
                        obj.Delete(Console.ReadLine());
                        break;
                    case 7:
                        Console.Clear();
                        Helper.WriteToFile(obj);
                        break;
                }
            }
        }
    }
}
