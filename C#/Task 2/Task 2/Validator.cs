using System;

namespace Manage_class_Flight
{
    class Validator
    {
        // Class properties validation
        public static int VerifyID(int value)
        {
            if (value > 0)
            {
                return value;
            }
            throw new Exception($"Incorrect ID format: {value}. ID can only be positive integer number");
        }

        public static string VerifyCountry(string value)
        {
            if (Enum.IsDefined(typeof(Countries), value))
            {
                return value;
            }
            throw new Exception($"Incorrect Country data: {value}. This country is not in Enum");
        }

        public static DateTime VerifyTime(DateTime dep, DateTime arr)
        {
            if (dep < arr && (dep > DateTime.Now || arr > DateTime.Now))
            {
                return arr;
            }
            throw new Exception($"Incorrect DateTime Format. Either departure happened after arrival\n" +
                $"or either departure or arrival happened earlier this exact moment");
        }

        public static float VerifyPrice(float value)
        {
            if (value > 0)
            {
                return (float)Math.Round(value * 100f) / 100f;
            }
            throw new Exception($"Incorrect price format: {value}. Price can only be positive floating point number");
        }

        public static string VerifyCompany(string value)
        {
            if (Enum.IsDefined(typeof(Companies), value))
            {
                return value;
            }
            throw new Exception($"Incorrect Company data: {value}. This company is not in Enum");
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