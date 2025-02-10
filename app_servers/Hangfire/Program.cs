using Microsoft.EntityFrameworkCore;
using Hangfire.Models.Jobs.GitRepo;

var builder = WebApplication.CreateBuilder(args);

var connectionString = "server=localhost;user=root;password=root;database=localhost";
var serverVersion = ServerVersion.AutoDetect(connectionString);

// Add services to the container.

builder.Services.AddControllers();
// builder.Services.AddDbContext<GitRepoContext>(opt =>
//     opt.UseMySql(builder.Configuration.GetConnectionString("DefaultConnection")));

builder.Services.AddDbContext<GitRepoContext>(opt => opt.UseMySql(connectionString, serverVersion));
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
