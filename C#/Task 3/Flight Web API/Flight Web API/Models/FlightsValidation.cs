using System;
using System.ComponentModel.DataAnnotations;

namespace Flight_Web_API.Models
{
    enum Countries
    {
        Ukraine, France, Italy, England, USA, Japan, Germany
    }

    enum Companies
    {
        Ryanair, Wizzair, ANA, EVA
    }

    public class CountryValidation : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if (Enum.IsDefined(typeof(Countries), value))
                return ValidationResult.Success;
            else
                return new ValidationResult($"Country {value} is not defined in enum");
        }
    }

    public class CompanyValidation : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if (Enum.IsDefined(typeof(Companies), value))
                return ValidationResult.Success;
            else
                return new ValidationResult($"Company {value} is not defined in enum");
        }
    }

    public class TicketPriceValidation : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if ((decimal)value > 0) {
                Math.Round((decimal)value, 2);
                return ValidationResult.Success;
            }
            else
                return new ValidationResult("Price can't be negative");
        }
    }

    public class DepartureTimeValidation : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if ((DateTime)value > DateTime.Now)
                return ValidationResult.Success;
            else
                return new ValidationResult("Had departure already happen?");
        }
    }

    public class ArrivalTimeValidation : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            DateTime departure = (DateTime)validationContext.ObjectType.GetProperty("DepartureTime").GetValue(validationContext.ObjectInstance, null);
            if ((DateTime)value > departure)
                return ValidationResult.Success;
            else
                return new ValidationResult("Arrival can't happen before departure");
        }
    }
}