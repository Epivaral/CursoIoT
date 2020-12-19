//Incluimos la liberaria para manejo del sensor DHT22
// disponible en: https://github.com/beegee-tokyo/DHTesp

#include "DHTesp.h" 

DHTesp dht;

void setup()
{
  Serial.begin(9600);

  dht.setup(D5, DHTesp::DHT22); // Inicializamos el sensor para usar el GPIO 5
}

void loop()
{
 
  float humedad = dht.getHumidity(); //Obtenemos la medicion de la humedad
  float temperatura = dht.getTemperature(); //Obtenemos la medicion de la temperatura

  //Desplegamos los valores
  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.print("% ");
  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" C");

  //Damos 2 segundos entre lectura
  delay(2000);

}
