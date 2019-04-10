
using Grpc.Core;
using Instrosetta.Interfaces.Debugging.Echo.V1;
using System.Threading.Tasks;

namespace Instrosetta.Servers.Debugging.EchoServer.V1
{
    public class EchoImpl : EchoService.EchoServiceBase
    {
        public override Task<EchoResponse> Echo(EchoRequest request, ServerCallContext context)
        {
            EchoResponse response = new EchoResponse {Name = request.Name, Message = request.Message };
            return Task.FromResult(response);
        }
    }
}

