using Microsoft.IdentityModel.Tokens;
using System.Text;

namespace Flight_Web_API
{
    public class AuthOptions
    {
        public const string ISSUER = "server";
        public const string AUDIENCE = "client";
        public const int LIFETIME = 5;

        private const string KEY = "use_this_to_make_things_go_wild";
        
        public static SymmetricSecurityKey GetSymmetricSecurityKey() => 
            new SymmetricSecurityKey(Encoding.ASCII.GetBytes(KEY));
    }
}