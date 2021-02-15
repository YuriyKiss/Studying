using System;

namespace Manage_class_Flight
{
    class Validator
    {
        public static int VerifyID(int value)
        {
            try 
            {
                if (value <= 0)
                {
                    Console.WriteLine("ID can't be lesser 1");
                    return -1;
                }
                return value;
            }
            catch
            {
                Console.WriteLine("Exception reading ID occured");
                return -1;
            }
        }

        public static string VerifyCountry(string value)
        {
            try
            {
                if (!Enum.IsDefined(typeof(Countries), value))
                {
                    Console.WriteLine("Country is not in Enum");
                    return "invalid";
                }
                return value;
            }
            catch
            {
                Console.WriteLine("Exception occured, while validating Countries");
                return "invalid";
            }
        }

        public static DateTime VerifyTime(DateTime dep, DateTime arr)
        {
            if (dep >= arr)
            {
                Console.WriteLine("Departure happened later than arrival");
                return new DateTime(1900, 1, 1, 0, 0, 0);
            }
            if (dep < DateTime.Now || arr < DateTime.Now)
            {
                Console.WriteLine("Flight already happened?");
                return new DateTime(1900, 1, 1, 0, 0, 0);
            }
            return dep;
        }

        public static float VerifyPrice(float price)
        {
            try
            {
                if (price <= 0)
                {
                    Console.WriteLine("You can't fly for free!");
                    return -1;
                }
                return (float)Math.Round(price * 100f) / 100f;
            }
            catch
            {
                Console.WriteLine("Exception occured while validating price");
                return -1;
            }
        }

        public static string VerifyCompany(string value)
        {
            try
            {
                if (!Enum.IsDefined(typeof(Companies), value))
                {
                    Console.WriteLine("Company is not in Enum\n");
                    return "invalid";
                }
                return value;
            }
            catch (Exception)
            {
                Console.WriteLine("Exception occured, while validating Companies\n");
                return "invalid";
            }
        }
    }


    public enum Countries
    {
        Ukraine = 1, Japan = 2, USA = 3, France = 4, Italy = 5, Germany = 6, England = 7, Switzerland = 8
    };


    public enum Companies
    {
        Ryanair = 1, Wizzair = 2, ENN = 3, ANA = 4
    };
}
