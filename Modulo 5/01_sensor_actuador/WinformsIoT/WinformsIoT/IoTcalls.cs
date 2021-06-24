//Codigo basado en quickstarts de Microsoft: https://docs.microsoft.com/en-us/learn/modules/remotely-monitor-devices-with-azure-iot-hub/

using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Devices;

namespace WinformsIoT
{
    class IoTcalls
    {
        public static string ReturnMessage = "";
        //Declare the class to send methods to devices
        private static ServiceClient serviceClient;

        // Connection string for your IoT Hub
        private readonly static string s_connectionString = "HostName=ioTSwfdygjgjgourData.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=+ub456456w10K9grtrtyrdfQr0EvIL686jghYVM=";
        static string targetDevice = "ESP8266Demo";

        

        

        public async static Task SendCloudToDeviceMessageAsync(string msg)
        {
            serviceClient = ServiceClient.CreateFromConnectionString(s_connectionString);

            var commandMessage = new
             Message(Encoding.ASCII.GetBytes(msg));
            await serviceClient.SendAsync(targetDevice, commandMessage);
        }
    }
}
