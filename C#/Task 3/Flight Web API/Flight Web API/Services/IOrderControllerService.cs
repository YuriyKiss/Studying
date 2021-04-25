using System.Security.Claims;
using System.Collections.Generic;

using Microsoft.AspNetCore.Mvc;

using Flight_Web_API.Models;

namespace Flight_Web_API.Sevices
{
    public interface IOrderControllerService
    {
        public int Create(Order toAdd, string username);
        public Order GetOrder(int id, string username);
        public List<Order> GetOrders(string username);
    }
}