var builder = WebApplication.CreateBuilder(args);

// Controller’ları kullanacağımızı söylüyoruz
builder.Services.AddControllers();

// Swagger (test ekranı) için – isterlerse dursun
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

// Controller’ları API olarak ayağa kaldır
app.MapControllers();

app.Run();
