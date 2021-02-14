using System;
using System.Collections.Generic;
using System.Text;

namespace Manage_class_Flight
{
    class Collection
    {
        // Constructors
        public Collection()
        {
            Coll = new List<Flight>();
        }

        public Collection(List<Flight> data)
        {
            Coll = data;
        }

        // Properties
        public List<Flight> Coll { get; set; }

        // Functions override
        public override string ToString()
        {
            string resp = "";
            foreach (Flight a in Coll)
            {
                resp += a.ToString() + "\n";
            }
            return resp;
        }
    }
}
