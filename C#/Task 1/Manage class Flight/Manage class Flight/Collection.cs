using System.Collections.Generic;

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

        // Integrity check
        public void VerifyData()
        {
            List<Flight> delete_later = new List<Flight>();
            foreach(Flight f in Coll)
            {
                if (!f.Verify())
                {
                    delete_later.Add(f);
                }
            }
            foreach(Flight f in delete_later)
            {
                Coll.Remove(f);
            }
        }
    }
}
