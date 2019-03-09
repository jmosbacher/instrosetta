using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Grpc.Core;

namespace Devices.Motion.Linear.Singleaxis
{
    class Program
    {
        static void Main(string[] args)
        {
            int Port = 50052;
            bool Debug = true;

            
            if (args.Length > 0)
            {
                Int32.TryParse(args[0], out Port);
            }
            if (args.Length > 1)
            {
                bool.TryParse(args[1], out Debug);
            }
            SingleLinearAxisImpl impl = new SingleLinearAxisImpl(Debug);

            Server server = new Server
            {
                Services = { SingleLinearAxis.BindService(impl) },
                Ports = { new ServerPort("localhost", Port, ServerCredentials.Insecure) }
            };
            server.Start();

            Console.WriteLine("RouteGuide server listening on port " + Port);
            Console.WriteLine("Press any key to stop the server...");
            Console.ReadKey();
            impl.Disconnect();
            

            server.ShutdownAsync().Wait();
        }
    }
}
