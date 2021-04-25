using System;
using System.ComponentModel.DataAnnotations;

namespace Flight_Web_API.Models
{
    public partial class Order
    {
        [Key]
        [Range(0, Int32.MaxValue, ErrorMessage = "The field {0} must be greater than {1}.")]
        public int? ID { get; set; }

        public string Username { get; set; }

        [Required]
        public int FlightID { get; set; }

        [Required]
        [Range(0, Int32.MaxValue, ErrorMessage = "Places {0} must be greater than {1}.")]
        public int Places { get; set; }

        public DateTime Date { get; set; }
    }
}