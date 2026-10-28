using Microsoft.AspNetCore.Mvc;
using MyApi.Models;
using System.Collections.Generic;
using System.Linq;

namespace MyApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ProductController : ControllerBase
    {
        // Sanki veritabanı varmış gibi davranacağımız sahte liste
        private static List<Product> _products = new List<Product>()
        {
            new Product { Id = 1, Name = "Laptop",  Price = 15000, Stock = 5,  Category = "Elektronik" },
            new Product { Id = 2, Name = "Telefon", Price = 20000, Stock = 10, Category = "Elektronik" },
            new Product { Id = 3, Name = "Kitap",   Price = 50,    Stock = 100,Category = "Kültür" }
        };

        // Şimdilik: Tüm ürünleri dönen basit GET endpoint
        [HttpGet]
        public ActionResult<IEnumerable<Product>> GetAll()
        {
            return Ok(_products);
        }
        [HttpGet("filter")]
        public ActionResult<IEnumerable<Product>> Filter(
            [FromQuery] string? name,
            [FromQuery] decimal? minPrice,
            [FromQuery] decimal? maxPrice,
            [FromQuery] int? minStock,
            [FromQuery] int? maxStock,
            [FromQuery] string? category
        )
        {
            var query = _products.AsEnumerable();
            if(!string.IsNullOrWhiteSpace(name))
            {
                var lowerName=name.ToLower();
                query=query.Where(p=> p.Name.ToLower().Contains(lowerName));
            }
            if(minPrice.HasValue){
                query=query.Where(p=> p.Price>=minPrice.Value);
            }
            if(maxPrice.HasValue){
                query=query.Where(p=> p.Price<=maxPrice.Value);
            }
            if(minStock.HasValue){
                query=query.Where(p=> p.Stock>=minStock.Value);
            }
            if(maxStock.HasValue){
                query=query.Where(p=> p.Stock<=maxStock.Value);
            }
            if(!string.IsNullOrWhiteSpace(category))
            {
                var lowerCat=category.ToLower();
                query=query.Where(p=> p.Category.ToLower()== lowerCat);
            }
            return Ok(query.ToList());
        }
        [HttpGet("{id}")]
        public ActionResult<IEnumerable<Product>> GetById(int id){
            var product = _products.FirstOrDefault(p=> p.Id == id);
            if(product==null)
            {
                return NotFound();
            }
            return Ok(product);
        }
        [HttpPost]
        public ActionResult<IEnumerable<Product>> Create([FromBody] Product product)
        {
            if(!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            int newId = _products.Any() ? _products.Max(p=> p.Id) + 1 : 1;
            product.Id = newId;

            _products.Add(product);
            return CreatedAtAction(nameof(GetById),new {id=product.Id},product);
        }
        [HttpPut("{id}")]
        public ActionResult<IEnumerable<Product>> Update(int id,[FromBody] Product updatedProduct)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            var product= _products.FirstOrDefault(p=> p.Id ==id);
            if (product==null)
            {
                return NotFound($"Id={id} ürünü bulunamadi.");
            }
            product.Name=updatedProduct.Name;
            product.Price=updatedProduct.Price;
            product.Stock=updatedProduct.Stock;
            product.Category=updatedProduct.Category;
            return NoContent();
        }
        [HttpDelete("{id}")]
        public ActionResult Delete(int id)
        {
            var product = _products.FirstOrDefault(p=> p.Id==id);
            if (product==null)
            {
                return NotFound($"Id={id} ürünü bulunamadi.");
            }
            _products.Remove(product);
            return NoContent();
        }

    }
}
