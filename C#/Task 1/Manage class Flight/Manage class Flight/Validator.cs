using System;
using System.Collections.Generic;
using System.Text;

namespace Manage_class_Flight
{
    class Validator
    {
        public static int VerifyID(int value)
        {
            if (value.GetType().Equals(typeof(int)))
            {
                if (value <= 0)
                {
                    Console.WriteLine($"ID should not be (lesser than)/(equal to) zero. Current - {value}");
                    return -1;
                }
                return value;
            }
            else
            {
                Console.WriteLine("Type of value must be int");
                return -1;
            }
        }
    }
}
