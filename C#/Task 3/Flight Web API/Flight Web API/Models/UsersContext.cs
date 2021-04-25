using Microsoft.EntityFrameworkCore;

namespace Flight_Web_API.Models
{
    public class UsersContext : DbContext
    {
        public UsersContext() { }

        public UsersContext(DbContextOptions<UsersContext> options) : base(options) { }

        public DbSet<User> Users { get; set; }
    }
}