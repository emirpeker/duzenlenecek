using System.ComponentModel.DataAnnotations;

namespace MyApi.Models
{
    public class Product
    {
        public int Id { get; set; }
        [Required(ErrorMessage = "Ürün adı boş olamaz.")]
        public string Name { get; set; } = string.Empty;
        [Range(0.01, double.MaxValue, ErrorMessage = "Fiyat 0'dan büyük olmalıdır.")]
        public decimal Price { get; set; }
        [Range(0, int.MaxValue, ErrorMessage = "Stok 0'dan küçük olamaz.")]
        public int Stock { get; set; }
        [Required(ErrorMessage = "Kategori boş olamaz.")]
        public string Category { get; set; } = string.Empty;
    }
}
