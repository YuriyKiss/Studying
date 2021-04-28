using Microsoft.EntityFrameworkCore;

namespace Flight_Web_API.Models
{
    public class OrdersContext : DbContext
    {
        public OrdersContext() { }

        public OrdersContext(DbContextOptions<OrdersContext> options) : base(options) { }

        public DbSet<Order> Orders { get; set; }
    }
}