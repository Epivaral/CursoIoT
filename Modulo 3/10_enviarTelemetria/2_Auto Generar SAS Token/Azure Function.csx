    //code from https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-security#security-tokens
    
    #r "Newtonsoft.Json"

    using System;
    using System.Net;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.Extensions.Primitives;
    using Newtonsoft.Json;
    using System.Globalization;
    using System.Net.Http;
    using System.Security.Cryptography;
    using System.Text;

    public static async Task<IActionResult> Run(HttpRequest req, ILogger log)
    {

         log.LogInformation("C# HTTP trigger function processed a request.");
         string token = "";
         try
         {
            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);
            int expiryInSeconds = (int)data?.expiryInSeconds;
            string resourceUri = data?.resourceUri;
            string key = data?.key;
            string policyName = data?.policyName;
            TimeSpan fromEpochStart = DateTime.UtcNow - new DateTime(1970, 1, 1);
            string expiry = Convert.ToString((int)fromEpochStart.TotalSeconds + expiryInSeconds);
            string stringToSign = WebUtility.UrlEncode(resourceUri) + "\n" + expiry;
            HMACSHA256 hmac = new HMACSHA256(Convert.FromBase64String(key));
            string signature = Convert.ToBase64String(hmac.ComputeHash(Encoding.UTF8.GetBytes(stringToSign)));
            token = String.Format(CultureInfo.InvariantCulture, "SharedAccessSignature sr={0}&sig={1}&se={2}", WebUtility.UrlEncode(resourceUri), WebUtility.UrlEncode(signature), expiry);
            if (!String.IsNullOrEmpty(policyName))
              {
                token += "&skn=" + policyName;
              }
         }
         catch(Exception ex)
         {
            return (ActionResult)new OkObjectResult($"{ex.Message}");
         }
         return (ActionResult)new OkObjectResult($"{token}");
    }