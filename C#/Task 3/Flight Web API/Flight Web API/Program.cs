using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Flight_Web_API
{
    public class Program
    {
        public static void Main() => 
            CreateHostBuilder().Build().Run();

        public static IHostBuilder CreateHostBuilder() =>
            Host.CreateDefaultBuilder().
            ConfigureWebHostDefaults(
                webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                }
            );
    }
}
