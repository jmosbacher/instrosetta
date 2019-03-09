using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Globalization;
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

        private void CheckConnection()
        {
            if (_Motor == null || !_Motor.Connected) {
                Status stat = new Status(StatusCode.Unavailable, "Not connected. \n");
                Metadata meta = new Metadata
                        {
                            { "help", "Check that device is present and try calling Connect method again."}
                        };
                throw new RpcException(stat, meta);
            }
        }
        public SingleLinearAxisImpl(bool debug)
        {
            if (debug)
            {
                SimulationManager.Instance.InitializeSimulations();
            }
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

            int timeout = (int)(request.Timeout * 1000); //UnitConverter.ConvertByAbbreviation(request.Timeout, "Time", "s", "ms");
            int interval = (int)(request.PollingInterval * 1000); //UnitConverter.ConvertByAbbreviation(request.PollingInterval, "Time", "s", "ms");
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
            CheckConnection();


            try
            {
                Device dev = new Device { SerialNumber = UInt32.Parse(_Motor.SerialNo) };
                _Motor.Disconnect();
                SimulationManager.Instance.UninitializeSimulations();
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
            CheckConnection();
     

            var limits = _Motor.GetRange();
        
            var min = UnitConverter.ConvertByAbbreviation(limits.Item1, "Length", request.Units, "mm");
            var max = UnitConverter.ConvertByAbbreviation(limits.Item2, "Length", request.Units, "mm");
            StageRange rng = new StageRange {
                Min = min,
                Max = max,
                Resolution = (double) _Motor.Resolution,
                Units = "mm",
                };
            return Task.FromResult(rng);
        }

        public override Task<Position> GetPosition(GetPositionRequest request, ServerCallContext context)
        {
            CheckConnection();
            Position position = new Position
            {
                Value = (double) _Motor.Position,
                Units = "mm",
            };
            return Task.FromResult(position);
        }

        private async Task StreamPosition(IServerStreamWriter<Position> responseStream)
        {
            do
            {
                double position = (double)_Motor.Position;
                position = (double)_Motor.Position;
                Position response = new Position
                {
                    Value = position,
                    Units = "mm"

                };

                await responseStream.WriteAsync(response);
                Thread.Sleep(300);

            } while (_Motor.State == MotorState.MOVING);
        }

        public override async Task MoveAbsolute(MoveAbsoluteRequest request, IServerStreamWriter<Position> responseStream, ServerCallContext context)
        {
            CheckConnection();

            // decimal destination = (decimal) UnitConverter.ConvertByAbbreviation(request.Position.Value, "Length", request.Position.Units, "Millimeter");
            decimal destination = (decimal) request.Position.Value;
            

            _Motor.MoveAbsolute(destination);
            await StreamPosition(responseStream);
            _Motor.ThrowLastDeviceException();
            

        }

        public override async Task MoveRelative(MoveRelativeRequest request, IServerStreamWriter<Position> responseStream, ServerCallContext context)
        {

            CheckConnection();

            if (request.Distance.Direction.ToString() == "undefined")
            {
                Status stat = new Status(StatusCode.InvalidArgument, "Direction undefined.");
                Metadata meta = new Metadata
                        {
                            { "valid_options", "1,2" }
                        };
                throw new RpcException(stat, meta);
            }

            decimal distance = (decimal) request.Distance.Value;
            _Motor.MoveRelative((MotorDirection) request.Distance.Direction, distance, 5000);

            await StreamPosition(responseStream);
            _Motor.ThrowLastDeviceException();

        }

    }


}
