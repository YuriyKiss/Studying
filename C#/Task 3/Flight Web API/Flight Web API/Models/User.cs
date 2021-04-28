using System;
using System.ComponentModel.DataAnnotations;

namespace Flight_Web_API.Models
{
    public partial class User
    {
        [Key]
        [LoginValidation]
        public string Login { get; set; }

        [Required]
        [StringLength(32, MinimumLength = 6)]
        public string Password { get; set; }

        public string Role { get; set; }
    }
}