using System;
using System.Reflection;

namespace Manage_class_Flight
{
    class Flight
    {
        // Properties
        private int _id;
        private string _dep_c, _arr_c;
        private DateTime _dep_t, _arr_t;
        private float _tick;
        private string _com_n;

        // Contructors
        public Flight() { }

        public Flight(int id, string dep_c, string arr_c, DateTime dep_t, 
                      DateTime arr_t, float tick, string com_n)
        {
            ID = id;
            DepartureCountry = dep_c;
            ArrivalCountry = arr_c;
            DepartureTime = dep_t;
            ArrivalTime = arr_t;
            TicketPrice = tick;
            CompanyName = com_n;
        }

        // Setters and Getters
        public int ID 
        {
            set { _id = Validator.VerifyID(value); }
            get { return _id; }
        }
        public string DepartureCountry 
        {
            set { _dep_c = Validator.VerifyCountry(value); }
            get { return _dep_c; } 
        }
        public string ArrivalCountry 
        { 
            set { _arr_c = Validator.VerifyCountry(value); }
            get { return _arr_c; }
        }
        public DateTime DepartureTime 
        {
            set { _dep_t = value; }
            get { return _dep_t; } 
        }
        public DateTime ArrivalTime 
        { 
            set { _arr_t = Validator.VerifyTime(DepartureTime, value); } 
            get { return _arr_t; } 
        }
        public float TicketPrice 
        { 
            set { _tick = Validator.VerifyPrice(value); }
            get { return _tick; }
        }
        public string CompanyName 
        { 
            set { _com_n = Validator.VerifyCompany(value); }
            get { return _com_n; }
        }

        // Functions override
        public override string ToString()
        {
            PropertyInfo[] flp = Type.GetType(typeof(Flight).ToString()).GetProperties();

            string answer = "";
            foreach(PropertyInfo pi in flp)
            {
                answer += pi.Name + ": " + pi.GetValue(this, null) + "\n";
            }
            return answer;
        }
    }
}