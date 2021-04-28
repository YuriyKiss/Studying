using System.Linq;
using System.Text;
using System.Security.Claims;
using System.Collections.Generic;
using System.Security.Cryptography;

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
            toAdd.Password = ComputeSha256Hash(toAdd.Password);
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
            User person = context.Users.FirstOrDefault(x => x.Login == username && x.Password == ComputeSha256Hash(password));
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

        static string ComputeSha256Hash(string rawData)
        {
            using (SHA256 sha256Hash = SHA256.Create())
            {
                byte[] bytes = sha256Hash.ComputeHash(Encoding.UTF8.GetBytes(rawData));

                StringBuilder builder = new StringBuilder();
                for (int i = 0; i < bytes.Length; i++)
                    builder.Append(bytes[i].ToString("x2"));

                return builder.ToString();
            }
        }
    }
}