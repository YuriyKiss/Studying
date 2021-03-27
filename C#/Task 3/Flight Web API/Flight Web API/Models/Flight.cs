using System;
using System.ComponentModel.DataAnnotations;

namespace Flight_Web_API.Models
{
    public partial class Flight
    {
        [Key]
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
    }
}