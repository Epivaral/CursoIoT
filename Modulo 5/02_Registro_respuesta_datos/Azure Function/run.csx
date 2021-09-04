using System;
using Microsoft.Azure.Devices;
using System.Text;
using System.Data.SqlClient;


public static void Run(TimerInfo myTimer, ILogger log)
{

    //Declare the class to send methods to devices
    ServiceClient serviceClient;

    // Connection string for your IoT Hub
    // Azure Portal > IoT hub > Shared access policies > service > Primary connection string
    string s_connectionString = "HostName=ioTStudyYourData.azure-devices.net;SharedAccessKeyName=service;SharedAccessKey=+ubYRQ7j/BmCBJwdfgdfgdfg3HFedfQr0EvILBSxviSYVM=";
    string targetDevice = "ESP8266Demo";

    serviceClient = ServiceClient.CreateFromConnectionString(s_connectionString);

    SqlConnection conn = new SqlConnection("Server=tcp:studyyourdata.database.windows.net,1433;Initial Catalog=iot;Persist Security Info=False;User ID=<USR>;Password=<PWD>;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;");
    conn.Open();

    SqlCommand command = new SqlCommand("select FORMAT( getdate(), 'dd/MM/yy HH:mm' ) as fecha", conn);

    using (SqlDataReader reader = command.ExecuteReader())
    {
    if (reader.Read())
    {
        var commandMessage = new
                Message(Encoding.ASCII.GetBytes(reader.GetString(0)));
            serviceClient.SendAsync(targetDevice, commandMessage);
    }
    }

    conn.Close();
        
}