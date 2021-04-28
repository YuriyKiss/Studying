using System;
using System.ComponentModel.DataAnnotations;

namespace Flight_Web_API.Models
{
    public partial class Flight
    {
        [Key]
        [Range(0, Int32.MaxValue, ErrorMessage = "The field {0} must be greater than {1}.")]
        public int ID { get; set; }

        [Required]
        [CountryValidation]
        public string DepartureCountry { get; set; }

        [Required]
        [CountryValidation]
        public string ArrivalCountry { get; set; }

        [Required]
        [DepartureTimeValidation]
        public DateTime DepartureTime { get; set; }

        [Required]
        [ArrivalTimeValidation]
        public DateTime ArrivalTime { get; set; }

        [Required]
        [TicketPriceValidation]
        public decimal TicketPrice { get; set; }

        [Required]
        [CompanyValidation]
        public string CompanyName { get; set; }

        [Required]
        [Range(0, Int32.MaxValue, ErrorMessage = "Places {0} must be greater than {1}.")]
        public int Places { get; set; }
    }
}