﻿using System;
using System.Collections.Generic;
using System.Text;
using Grpc.Core;
using Devices.Motion.Linear.Singleaxis;


namespace ThorlabsKDC101ServerGUI
{
    public class ThorlabsKDC101Server
    {
        private bool _Serving = false;
        private Server _Server = null;
        private ThorlabsKDC101ServerImpl _Impl = null;

        public void StartServing(string serveAddress, int port)
        {
            if (_Serving)
            {
                return;

            }
            else
            {
                _Impl = new ThorlabsKDC101ServerImpl();
                _Server = new Server
                {
                    Services = { SingleLinearAxis.BindService(_Impl) },
                    Ports = { new ServerPort(serveAddress, port, ServerCredentials.Insecure) }
                };
                _Server.Start();
                _Serving = true;

            }
        }

        public void StopServing()
            {
                _Impl.Disconnect();
                _Server.ShutdownAsync().Wait();
                _Server = null;
                _Impl = null;
                _Serving = false;

            }


        }

}
