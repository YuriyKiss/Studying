using Microsoft.EntityFrameworkCore;

namespace Flight_Web_API.Models
{
    public class FlightsContext : DbContext
    {
        public FlightsContext() { }

        public FlightsContext(DbContextOptions<FlightsContext> options) : base(options) { }

        public DbSet<Flight> Flights { get; set; }
    }
}