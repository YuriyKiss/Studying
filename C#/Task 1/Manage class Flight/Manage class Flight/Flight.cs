using System;

namespace Manage_class_Flight
{
    class Flight
    {
        // Contructors
        public Flight()
        {
            ID = -1;
            DepartureCountry = "invalid";
            ArrivalCountry = "invalid";
            DepartureTime = new DateTime(1900, 1, 1, 0, 0, 0);
            ArrivalTime = new DateTime(1900, 1, 1, 0, 0, 0);
            TicketPrice = -1;
            CompanyName = "invalid";
        }

        public Flight(int id, string dep_count, string arr_count, DateTime dep_time, 
                      DateTime arr_time, float tick, string comp)
        {
            ID = id;
            DepartureCountry = dep_count;
            ArrivalCountry = arr_count;
            DepartureTime = dep_time;
            ArrivalTime = arr_time;
            TicketPrice = tick;
            CompanyName = comp;
        }

        // Setters and Getters
        public int ID { set; get; }
        public string DepartureCountry { set; get; }
        public string ArrivalCountry { set; get; }
        public DateTime DepartureTime { set; get; }
        public DateTime ArrivalTime { set; get; }
        public float TicketPrice { set; get; }
        public string CompanyName { set; get; }

        // Functions override
        public override string ToString()
        {
            return $"Flight ID - {ID}\nFlight path: {DepartureCountry} - {ArrivalCountry}\n" +
                $"Flight time: {(ArrivalTime - DepartureTime).Hours} hrs {(ArrivalTime - DepartureTime).Minutes} min\n" +
                $"Departure Time: {DepartureTime}\nTicket by {CompanyName} - {TicketPrice} UAH\n";
        }

        // Integrity check
        public bool Verify()
        {
            ID = Validator.VerifyID(ID);
            DepartureCountry = Validator.VerifyCountry(DepartureCountry);
            ArrivalCountry = Validator.VerifyCountry(ArrivalCountry);
            DepartureTime = Validator.VerifyTime(DepartureTime, ArrivalTime);
            TicketPrice = Validator.VerifyPrice(TicketPrice);
            CompanyName = Validator.VerifyCompany(CompanyName);


            return (ID != -1 && DepartureCountry != "invalid" && ArrivalCountry != "invalid"
                && DepartureTime != new DateTime(1900, 1, 1, 0, 0, 0) && ArrivalTime != new DateTime(1900, 1, 1, 0, 0, 0)
                && TicketPrice != -1 && CompanyName != "invalid");
        }

        public Flight DeepCopy()
        {
            Flight deepcopyFlight = new Flight(ID, DepartureCountry, ArrivalCountry, 
                DepartureTime, ArrivalTime, TicketPrice, CompanyName);

            return deepcopyFlight;
        }
    }
}