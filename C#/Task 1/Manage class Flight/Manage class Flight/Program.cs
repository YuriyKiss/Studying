using System;

namespace Manage_class_Flight
{
    class Program
    {
        static void Main()
        {   
            Collection obj = Helper.GetCollectionFromJson();

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
                        break;
                    case 3:
                        break;
                    case 4:
                        break;
                    case 5:
                        break;
                    case 6:
                        break;
                    case 7:
                        break;
                }
            }
        }
    }
}
