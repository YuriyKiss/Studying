using System;
using System.Linq;
using System.Text;
using System.Security.Claims;
using System.Collections.Generic;

using Flight_Web_API.Models;

namespace Flight_Web_API.Sevices
{
    public class OrderControllerService : IOrderControllerService
    {
        private OrdersContext context = new OrdersContext();

        public OrderControllerService(OrdersContext cont)
        {
            context = cont;
        }

        public int Create(Order toAdd, string username)
        {
            toAdd.ID = null;
            toAdd.Username = username;
            toAdd.Date = DateTime.Today;
            try
            {
                context.Orders.Add(toAdd);
                context.SaveChanges();
            }
            catch { return 404; }
            return 201;
        }

        public List<Order> GetOrders(string username)
        {
            List<Order> data = context.Orders.ToList();
            data.RemoveAll(x => x.Username != username);
            return data;
        }

        public Order GetOrder(int id, string username)
        {
            Order to_return = context.Orders.Find(id);
            if (to_return != null)
                if (to_return.Username == username)
                    return to_return;
            return null;
        }
    }
}