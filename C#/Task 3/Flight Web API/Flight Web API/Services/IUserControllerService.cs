using System.Security.Claims;
using Microsoft.AspNetCore.Mvc;

using Flight_Web_API.Models;

namespace Flight_Web_API.Sevices
{
    public interface IUserControllerService
    {
        public int Register(User toAdd);
        public ClaimsIdentity FindUser(string username, string password);
    }
}