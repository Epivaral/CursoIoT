// Codigo basado en quickstarts de Microsoft: https://docs.microsoft.com/en-us/learn/modules/remotely-monitor-devices-with-azure-iot-hub/



using System;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.Azure.EventHubs;
using System.Threading;

namespace WinformsIoT
{
    public partial class ControlarServos : Form
    {

        public ControlarServos()
        {
            InitializeComponent();
        }
        // console > built in endpoints > Event Hub-compatible endpoint

        private readonly static string s_eventHubsCompatibleEndpoint = "sb://ihsupajdaksds013dednamespace.servicebus.windows.net/";


        // Event Hub-compatible name
        // az iot hub show --query properties.eventHubEndpoints.events.path --name {your IoT Hub name}
        private readonly static string s_eventHubsCompatiblePath = "iothub-ehub-iotstuasddyyo-9693453533-b8g454794bde";

        // az iot hub policy show --name service --query primaryKey --hub-name {your IoT Hub name}
        private readonly static string s_iotHubSasKey = "+ubYRQ7j/BmCBJw1dsfgedfQr043t34345SyhdviSYVM=";
        private readonly static string s_iotHubSasKeyName = "service";
        private static EventHubClient s_eventHubClient;

        private async Task ReceiveMessagesFromDeviceAsync(string partition, CancellationToken ct)
        {

            var eventHubReceiver = s_eventHubClient.CreateReceiver("$Default", partition, EventPosition.FromEnqueuedTime(DateTime.Now));

            while (true)
            {
                if (ct.IsCancellationRequested) break;
                // Check for EventData - this methods times out if there is nothing to retrieve.
                var events = await eventHubReceiver.ReceiveAsync(100);

                // If there is data in the batch, process it.
                if (events == null) continue;

                foreach (EventData eventData in events)
                {
                    string data = Encoding.UTF8.GetString(eventData.Body.Array);
                    //Console.WriteLine("Message received on partition {0}:", partition);
                    //Console.WriteLine("  {0}:", data);
                    textBox1.AppendText(Environment.NewLine);
                    textBox1.AppendText("Lectura Sensor: "+data);
                }
            }
        }




        EventHubsConnectionStringBuilder connectionString;
        EventHubRuntimeInformation runtimeInfo;
        string[] d2cPartitions;
        CancellationTokenSource cts;


        private async void ControlarServos_Load(object sender, EventArgs e)
        {
            HabilitaControles(false);

            connectionString = new EventHubsConnectionStringBuilder(new Uri(s_eventHubsCompatibleEndpoint), s_eventHubsCompatiblePath, s_iotHubSasKeyName, s_iotHubSasKey);
            s_eventHubClient = EventHubClient.CreateFromConnectionString(connectionString.ToString());

            // Create a PartitionReciever for each partition on the hub.
            runtimeInfo = await s_eventHubClient.GetRuntimeInformationAsync();
            d2cPartitions = runtimeInfo.PartitionIds;
            cts = new CancellationTokenSource();

            HabilitaControles(true);

            foreach (string partition in d2cPartitions)
            {
                await ReceiveMessagesFromDeviceAsync(partition, cts.Token);
            }


        }

        private void HabilitaControles(bool valor)
        {

            label1.Visible = !valor;
        }

        

        
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            HabilitaControles(true);
        }

        

        

        private void Servo_Scroll(object sender, EventArgs e)
        {
            lblArriba.Text = Servo.Value.ToString()+ "°";
        }

      
        private async void Servo_MouseCaptureChanged(object sender, EventArgs e)
        {
            textBox1.AppendText(Environment.NewLine);
            textBox1.AppendText("Servo: "+ Servo.Value.ToString() + "°");

            string mensaje = Servo.Value.ToString();

            await IoTcalls.SendCloudToDeviceMessageAsync(mensaje);
        }
    }
}
