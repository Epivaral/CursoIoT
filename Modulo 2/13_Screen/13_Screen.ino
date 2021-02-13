//SSD1306 datasheet: https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf

//repositorio libreria https://github.com/ThingPulse/esp8266-oled-ssd1306
#include "SSD1306Wire.h"

//NODEMCU
//D1> SLC
//D2> SDA

//Direccion IIC para SSD1306 es 0x3c esto lo obtenemos del datasheet

SSD1306Wire  display(0x3c, D2, D1);

void setup() {
  display.init(); //inicializamos el display
  display.flipScreenVertically(); //damos vuelta a la imagen por la posicion de nuestra pantalla
}

int iteracion =0; //Desplegaremos el numero de iteracion que hagamos

void loop() {
  display.clear(); //Limpiamos lo que haya en pantalla

  //dibujamos un rectangulo con relleno
  //Parametros: posicion x, posicion Y, largo, ancho
  display.fillRect(0, 0, 128, 16);

  //definimos el color de escritura a "negro" para poder escribir sobre el rectangulo
  display.setColor(BLACK);
  
  /* tamanos de fuente validos: 
      ArialMT_Plain_10, 
      ArialMT_Plain_16,
      ArialMT_Plain_24
  */
  display.setFont(ArialMT_Plain_16);

  //Desplegamos un texto sobre el rectangulo
  //Parametros: posicion x, posicion Y, texto
  display.drawString(5, 0, "Modulo 11");


  //definimos el color de escritura a Blanco (el default)
  display.setColor(WHITE);
  
  // cambiamos tamano de fuente y desplegamos mensaje
  display.setFont(ArialMT_Plain_24);
  display.drawString(5, 25, "Iteracion "+String(iteracion++));
  
  //Mandamos al display lo que construimos en el buffer
  display.display();
  
  delay(1000);
}
