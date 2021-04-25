using System;
using System.Text.RegularExpressions;
using System.ComponentModel.DataAnnotations;

namespace Flight_Web_API.Models
{
    public class LoginValidation : ValidationAttribute
    {
        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if (Regex.Match((string)value, "[a-zA-Z][a-zA-Z._]{4,14}[a-zA-Z]").Success)
                return ValidationResult.Success;
            else
                return new ValidationResult($"Login {value} idoes not match regular expression");
        }
    }
}