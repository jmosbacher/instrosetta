using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.KCube.DCServoCLI;
using Thorlabs.MotionControl.GenericMotorCLI;

using Grpc.Core;
using Grpc.Core.Utils;
using UnitsNet;
using UnitsNet.Units;

namespace Devices.Motion.Linear.Singleaxis
{
    class SingleLinearAxisImpl : SingleLinearAxis.SingleLinearAxisBase

    {
        private KDC101 _Motor = null;
        private UnitParser _uparser = null; 

        public SingleLinearAxisImpl(bool debug=false)
        {
            _Motor = new KDC101(debug);
            _uparser = UnitParser.Default;
        }
        
        
        public override Task<TextMessage> Echo(TextMessage request, ServerCallContext context)
        {
            return Task.FromResult(request);
        }

        public override async Task ScanDevices(ScanDevicesRequest request, IServerStreamWriter<Device> responseStream, ServerCallContext context)
        {

            foreach (string serialNo in _Motor.GetAvailableDevices())
            {
                Device device = new Device
                {
                    SerialNumber = UInt32.Parse(serialNo),

                };
                await responseStream.WriteAsync(device);
            }



        }
        public override Task<Device> Connect(ConnectRequest request, ServerCallContext context)
        {
            if (_Motor != null)
            {
                if (_Motor.SerialNo == request.Device.SerialNumber.ToString())
                {
                    return Task.FromResult(request.Device);
                }
                else
                {
                    try
                    {
                        _Motor.Disconnect();
           
                    }
                    catch (Exception ex)
                    {
                        Status stat = new Status(StatusCode.Unavailable, "Failed to disconnect from current device." + ex.Message);
                        Metadata meta = new Metadata
                        {
                            { "exception_name", ex.GetType().Name }
                        };
                        throw new RpcException(stat, meta);
                    }

                }

            }

            int timeout = (int) TimeSpan.FromSeconds(request.Timeout).TotalMilliseconds;
            int interval = (int) TimeSpan.FromSeconds(request.PollingInterval).TotalMilliseconds;
            try
            {
                _Motor.Connect(request.Device.SerialNumber.ToString(), timeout, interval);
            }
            catch (Exception ex)
            {
                Status stat = new Status(StatusCode.NotFound, "Failed to connect to device. \n" + ex.Message);
                Metadata meta = new Metadata
                        {
                            { "exception_name", ex.GetType().Name }
                        };

                throw new RpcException(stat, meta);
            }
            
            return Task.FromResult(request.Device);

        }

        public Task<Device> Disconnect()
        {
            

            try
            {
                Device dev = new Device { SerialNumber = UInt32.Parse(_Motor.SerialNo) };
                _Motor.Disconnect();
                return Task.FromResult(dev);
            }
            catch (Exception ex)
            {
                Status stat = new Status(StatusCode.NotFound, "Failed to disconnect from device." + ex.Message);
                Metadata meta = new Metadata
                        {
                            { "exception_name", ex.GetType().Name }
                        };
                throw new RpcException(stat, meta);
            }

            

        }

        public override Task<StageRange> GetRange(GetRangeRequest request, ServerCallContext context)
        {
            
            var limits = _Motor.GetRange();
        
            var min = UnitConverter.ConvertByAbbreviation(limits.Item1, "Length", request.Units, "mm");
            var max = UnitConverter.ConvertByAbbreviation(limits.Item2, "Length", request.Units, "mm");
            StageRange rng = new StageRange {
                Min = min,
                Max = max,
                Units = "mm",
                };
            return Task.FromResult(rng);
        }


        public override async Task MoveAbsolute(MoveAbsoluteRequest request, IServerStreamWriter<Position> responseStream, ServerCallContext context)
        {
            
            decimal destination = (decimal) Length.Parse(String.Format("{0} {1}", request.Position.Value, request.Position.Units)).Millimeters;

            foreach (long position in _Motor.MoveAbsolute(destination)) {
                Position response = new Position
                {
                    Value = position,
                    Units = "mm"

                };
                await responseStream.WriteAsync(response);
            }

 

        }

        public override async Task MoveRelative(MoveRelativeRequest request, IServerStreamWriter<Position> responseStream, ServerCallContext context)
        {
            if (request.Distance.Direction.ToString() == "undefined")
            {
                Status stat = new Status(StatusCode.InvalidArgument, "Direction undefined.");
                Metadata meta = new Metadata
                        {
                            { "valid_options", "1,2" }
                        };
                throw new RpcException(stat, meta);
            }

            decimal distance = (decimal)Length.Parse(String.Format("{0} {1}", request.Distance.Value, request.Distance.Units)).Millimeters;

            foreach (long position in _Motor.MoveRelative((MotorDirection) request.Distance.Direction, distance, 5000))
            {
                Position response = new Position
                {
                    Value = position,
                    Units = "mm"

                };
                await responseStream.WriteAsync(response);
            }



        }

    }


}
