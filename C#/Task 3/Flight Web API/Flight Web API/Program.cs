using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting;

namespace Flight_Web_API
{
    public class Program
    {
        public static void Main() => CreateHostBuilder().Build().Run();

        public static IHostBuilder CreateHostBuilder() => Host.CreateDefaultBuilder().
            ConfigureWebHostDefaults(webBuilder => webBuilder.UseStartup<Startup>());
    }
}