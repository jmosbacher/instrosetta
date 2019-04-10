﻿using System;
using System.Collections.Generic;
using System.Text;
using Grpc.Core;
using Grpc.Reflection;
using Grpc.Reflection.V1Alpha;
using Instrosetta.Interfaces.MotionControl.Singleaxis;


namespace ThorlabsKDC101Server
{
    public class ThorlabsKDC101Server
    {
        private bool _Serving = false;
        private Server _Server = null;
        private ThorlabsKDC101ServerImpl _Impl = null;
        private ReflectionServiceImpl _Reflection = null;
        public void StartServing(string serveAddress, int port)
        {
            if (_Serving)
            {
                return;

            }
            else
            {
                _Impl = new ThorlabsKDC101ServerImpl();
                _Reflection = new ReflectionServiceImpl(SingleAxis.Descriptor, Echo.Descriptor, ServerReflection.Descriptor);
                _Server = new Server
                {
                    Services = { SingleAxis.BindService(_Impl),
                                 ServerReflection.BindService(_Reflection)},
                    Ports = { new ServerPort(serveAddress, port, ServerCredentials.Insecure) }
                };
                _Server.Start();
                _Serving = true;

            }
        }

        public void StopServing()
            {
            
            try
            {
                _Impl.OnExit();
            }
            catch (Exception ex)
            {

            }
            try
            {
                _Server.ShutdownAsync().Wait();
            }
            catch (Exception ex)
            {
                
            }
                
                _Server = null;
                _Impl = null;
                _Serving = false;

            }


        }

}
