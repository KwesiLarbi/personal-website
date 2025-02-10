using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using Pomelo.EntityFrameworkCore.MySql.Storage;
using System.Diagnostics;
using System.Linq;

namespace Hangfire.Models.Jobs.GitRepo
{
    public class GitRepoContext : DbContext
    {
        public GitRepoContext(DbContextOptions<GitRepoContext> options) : base(options)
        {
        }

        public DbSet<Project> Projects { get; set; }

        // protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        // {
        //     optionsBuilder
        //         .UseMySql("server=localhost;user=root;password=root;database=localhost",
        //             b => b.);
        // }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<Project>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.Property(e => e.Title).IsRequired();
                entity.Property(e => e.Description);
                entity.Property(e => e.GithubUrl).IsRequired();
                entity.Property(e => e.Language);
                entity.Property(e => e.Forks);
                entity.Property(e => e.Stars);
                entity.Property(e => e.SizeKB);
                entity.Property(e => e.CreatedAt).IsRequired();
                entity.Property(e => e.PushedAt);
                entity.Property(e => e.UpdatedAt);
            });
        }
    }
}
