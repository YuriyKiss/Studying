using System;
using System.Reflection;

namespace Manage_class_Flight
{
    public class Product
    {
        private string _title, _description, _imageUrl;
        private double _price;
        private DateTime _createdAt, _updatedAt;

        public Product() { ID = Guid.NewGuid(); }

        public Product(string title, string description, string imageUrl,
            double price, DateTime createdAt, DateTime updatedAt)
        {
            ID = Guid.NewGuid();
            Title = title;
            Description = description;
            ImageUrl = imageUrl;
            Price = price;
            CreatedAt = createdAt;
            UpdatedAt = updatedAt;
        }

        public Guid ID { get; }

        public string Title
        {
            get => _title;
            set => _title = Validation.ValidateName(value);
        }

        public string Description
        {
            get => _description;
            set => _description = value;
        }

        public string ImageUrl
        {
            get => _imageUrl;
            set => _imageUrl = Validation.ValidateUrl(value);
        }

        public DateTime CreatedAt
        {
            get => _createdAt;
            set => _createdAt = Validation.ValidateDate(value);
        }

        public DateTime UpdatedAt
        {
            get => _updatedAt;
            set => _updatedAt = Validation.ValidateDate(value, _createdAt);
        }

        public double Price
        {
            get => _price;
            set => _price = Validation.ValidatePrice(value);
        }


        public override string ToString()
        {
            string str = "";
            PropertyInfo[] props = this.GetType().GetProperties(
                BindingFlags.Instance | BindingFlags.Public);
            foreach (var prop in props)
            {
                str += $"{prop.Name}: {prop.GetValue(this)}  |  ";
            }

            return str;
        }
    }
}