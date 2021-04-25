using System.Linq;
using System.Security.Claims;
using System.Collections.Generic;

using Flight_Web_API.Models;

namespace Flight_Web_API.Sevices
{
    public class UserControllerService : IUserControllerService
    {
        private UsersContext context = new UsersContext();

        public UserControllerService(UsersContext cont)
        {
            context = cont;
        }

        public int Register(User toAdd)
        {
            toAdd.Role = "user";
            try
            {
                context.Users.Add(toAdd);
                context.SaveChanges();
            }
            catch { return 404; }
            return 201;
        }

        public ClaimsIdentity FindUser(string username, string password)
        {
            User person = context.Users.FirstOrDefault(x => x.Login == username && x.Password == password);
            if (person != null)
            {
                var claims = new List<Claim>
                {
                    new Claim(ClaimsIdentity.DefaultNameClaimType, person.Login),
                    new Claim(ClaimsIdentity.DefaultRoleClaimType, person.Role)
                };
                return new ClaimsIdentity(claims, "Token", ClaimsIdentity.DefaultNameClaimType, 
                                                           ClaimsIdentity.DefaultRoleClaimType);
            }
            return null;
        }
    }
}