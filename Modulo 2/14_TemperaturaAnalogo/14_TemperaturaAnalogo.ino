/*
 Utilizaremos el sensor de temperatura TMP36, el datasheet esta disponible aqui:
 https://cdn.sparkfun.com/datasheets/Sensors/Temp/TMP35_36_37.pdf

 segun el datasheet, obtenemos una lectura lineal, con el chip alimentado a 3.3V
debemos usar la formula:
   voltaje = (LecturaADC / 1024.0) * 3.3
   temperatura (C) = (voltaje - .5) * 100


SSD1306 datasheet: https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf   
 */


//repositorio libreria https://github.com/ThingPulse/esp8266-oled-ssd1306
#include "SSD1306Wire.h"

//NODEMCU
//D1> SLC
//D2> SDA

//Direccion IIC para SSD1306 es 0x3c esto lo obtenemos del datasheet

SSD1306Wire  display(0x3c, D2, D1);

const int PINADC = A0; // El pin A0 usado para ADC
int Lectura =0; //lectura obtenida del sensor TMP36


void setup() {
  display.init(); //inicializamos la pantalla
  display.flipScreenVertically(); //damos vuelta a la imagen por la posicion de nuestra pantalla
}

void DesplegarTemperatura(float temp)
{
  display.clear();//limpiamos lo que haya en pantalla en este momento
  
  // usamos una progress bar de la libreria para desplegar visualmente la temperatura
  //parametros: posicion x, posicion y, ancho x, ancho y, valor
  
  display.drawProgressBar(0, 32, 120, 10, temp);

  // desplegamos el valor numerico
  display.setTextAlignment(TEXT_ALIGN_CENTER);
  display.drawString(64, 15, String(temp) + "°C");
  display.display();
}

void loop() {
    Lectura = analogRead(PINADC);
    float voltaje = (Lectura / 1024.0) * 3.3;
    float temperatura = (voltaje - 0.5) * 100;

    DesplegarTemperatura(temperatura);

    delay(600);// pausa entre lecturas
}
