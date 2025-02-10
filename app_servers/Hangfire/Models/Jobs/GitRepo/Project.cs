using System;
using System.Reflection;
using Newtonsoft.Json;

namespace Hangfire.Models.Jobs.GitRepo
{
    public class Project
    {
        public int Id { get; set; }
        [JsonProperty("name")]
        public string? Title { get; set; }
        public string? Description { get; set; }
        [JsonProperty("html_url")]
        public string? GithubUrl { get; set; }
        public string? Language { get; set; }
        public int Forks { get; set; }
        [JsonProperty("stargazers_count")]
        public int Stars { get; set; }
        [JsonProperty("size")]
        public long SizeKB { get; set; }
        [JsonProperty("created_at")]
        public DateTime CreatedAt { get; set; }
        [JsonProperty("pushed_at")]
        public DateTime PushedAt { get; set; }
        [JsonProperty("updated_at")]
        public DateTime UpdatedAt { get; set; }
    }
}