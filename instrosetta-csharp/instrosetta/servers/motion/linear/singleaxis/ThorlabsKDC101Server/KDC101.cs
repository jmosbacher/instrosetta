using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

using Thorlabs.MotionControl.DeviceManagerCLI;
using Thorlabs.MotionControl.KCube.DCServoCLI;
using Thorlabs.MotionControl.GenericMotorCLI;
using UnitsNet.Units;
using Thorlabs.MotionControl.GenericMotorCLI.ControlParameters;

namespace Devices.Motion.Linear.Singleaxis
{
    class KDC101
    {

        private KCubeDCServo _kCubeDCServoMotor = null;
        private bool _Debug = false;


        public KDC101 (bool debug)
        {
            if (debug)
            {
                _Debug = true;
                
            }
            
        }

        public bool Connected
        {
            get
            {
                if (_kCubeDCServoMotor == null)
                {
                    return false;
                }
                else
                {
                    return true;
                }
            }
        }

        public decimal Position
        {
            get { return _kCubeDCServoMotor.Position; }
        }


        public string SerialNo
        {
            get { if (_kCubeDCServoMotor == null) {
                    return "0";

                    }
                else
                {
                    return _kCubeDCServoMotor.SerialNo;
                }
            }
        }

        public List<string> GetAvailableDevices()
        {
            List<string> serialNumbers = DeviceManagerCLI.GetDeviceList(KCubeDCServo.DevicePrefix);
            return serialNumbers;
        }

        public void Connect(string serialNo, int timeout, int interval)
        {
            if (_kCubeDCServoMotor != null)
            {
                if (_kCubeDCServoMotor.SerialNo == serialNo)
                {
                    return;
                }
                else
                {
                    Disconnect();
                    
                }

            }
            


            DeviceManagerCLI.BuildDeviceList();

            _kCubeDCServoMotor = KCubeDCServo.CreateKCubeDCServo(serialNo);

            // Establish a connection with the device.
            _kCubeDCServoMotor.Connect(serialNo);

            // Wait for the device settings to initialize. We ask the device to
            // throw an exception if this takes more than 5000ms (5s) to complete.
            _kCubeDCServoMotor.WaitForSettingsInitialized(timeout);

            // Initialize the DeviceUnitConverter object required for real world
            // unit parameters.
            _kCubeDCServoMotor.LoadMotorConfiguration(_kCubeDCServoMotor.DeviceID, DeviceConfiguration.DeviceSettingsUseOptionType.UseFileSettings);

            // This starts polling the device at intervals of 250ms (0.25s).
            _kCubeDCServoMotor.StartPolling(interval);

            // We are now able to enable the device for commands.
            _kCubeDCServoMotor.EnableDevice();

            return;

        }

        public void Disconnect()
        {
            if (!(_kCubeDCServoMotor == null)) {
                
                _kCubeDCServoMotor.StopPolling();
                _kCubeDCServoMotor.ShutDown();
                _kCubeDCServoMotor = null;
                

            }
   
            return;
            
            
            

        }

        public Tuple<decimal,decimal> GetRange()
        {
            
            LimitSwitchParameters realLP = _kCubeDCServoMotor.GetLimitSwitchParams();
            return Tuple.Create((decimal) realLP.AnticlockwiseHardwareLimit, (decimal) realLP.ClockwiseHardwareLimit);

        }

        private static bool _taskComplete;
        private static ulong _taskID;

        public static void CommandCompleteFunction(ulong taskID)
        {
            if ((_taskID > 0) && (_taskID == taskID))
            {
                _taskComplete = true;
            }
        }


        public IEnumerable <double> MoveAbsolute(decimal position)
        {
            _taskComplete = false;
            
            _taskID = _kCubeDCServoMotor.MoveTo(position, CommandCompleteFunction);
            Console.WriteLine("Starting move...");
            do
            {
                Thread.Sleep(500);
                double newPos = (double) _kCubeDCServoMotor.Position;
                Console.WriteLine("At "+ newPos.ToString());
                yield return newPos;

            } while (!_taskComplete);
            Console.WriteLine("Done.");
        }

        public IEnumerable<double> MoveRelative(MotorDirection direction, decimal distance, int timeout)
        {
            
               _taskComplete = false;
            _taskID = _kCubeDCServoMotor.MoveRelative(direction, distance, CommandCompleteFunction);
            Console.WriteLine("Starting move...");
            do
            {
                Thread.Sleep(500);
                double newPos = (double) _kCubeDCServoMotor.Position;
                Console.WriteLine("At " + newPos.ToString());
                yield return newPos;

            } while (!_taskComplete);
            Console.WriteLine("Done.");

        }

    }
}
