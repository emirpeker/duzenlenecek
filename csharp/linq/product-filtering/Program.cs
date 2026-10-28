using System;
using System.Collections.Generic;
using System.Linq;

public class Product
{
    public int Id { get; set;}
    public string Name { get; set; }=string.Empty;
    public int Price { get; set; }
    public string Category { get; set;}=string.Empty;
}

class Program
{
    static void Main()
    {
        List <Product> products= new List<Product>()
        {
            new Product {Id=1,Name="Laptop",Price=15000,Category="Elektronik"},
            new Product {Id=2,Name="Telefon",Price=20000,Category="Elektronik"},
            new Product {Id=3,Name="Kitap",Price=50,Category="Kültür"}
        };
        var newProduct = new Product {Id = 4,Name = "Mouse",Price = 300,Category = "Elektronik"};
        AddProduct(products, newProduct);
        foreach(var x in products){
            Console.WriteLine($"{x.Id} - {x.Name}");
        }

        var result=FilteredList(
            products,
            "lap",
            10000,
            20000,
            "Elektronik"
        );
        foreach(var x in result)
        {
            Console.WriteLine($"{x.Id} - {x.Name} - {x.Price} - {x.Category}");
        }
    }
    static void AddProduct(List<Product> list, Product newProduct)
    {
    list.Add(newProduct);
    }   
    static List<Product> FilteredList(
        List<Product> list,
        string name,
        decimal? minPrice,
        decimal? maxPrice,
        string category
    )
    {
        var query=list.AsEnumerable();
        if (!string.IsNullOrWhiteSpace(name))
        {
            var lowerName=name.ToLower();
            query=query.Where(p=> p.Name.ToLower().Contains(lowerName));
        }
        if (minPrice.HasValue)
        {
            query=query.Where(p=>p.Price>=minPrice.Value);
        }
        if (maxPrice.HasValue)
        {
            query=query.Where(p=>p.Price<=maxPrice.Value);
        }
        if(!string.IsNullOrWhiteSpace(category))
        {
            var lowerCat=category.ToLower();
            query=query.Where(p=> p.Category.ToLower().Contains(lowerCat));
        }
        return query.ToList();
    }
}