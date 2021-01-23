/*
 * La frecuencia de las notas musicales fue tomada de este sitio:
 * http://pages.mtu.edu/~suits/notefreqs.html
 * Los valores estan dados en hertz, que es el parametro que la funcion tone() usa.
 * NOTA: los valores fueron aproximados al entero superior mas cercano
 * 
 * 
 * El sensor de efecto hall US1881 funciona como un switch, afectado por el campo magnetico
 * el datasheet esta disponible en:
 * https://www.sparkfun.com/datasheets/Components/General/Hall-US1881EUA.pdf
 */



const int DO = 262;
const int RE = 294;
const int MI = 330;

const int PinBuzzer = 4; // GPIO que usaremos para el sonido
const int PINHall = 14; //EL GPIO pin que usaremos para el sensor
const int PINLed = 5; //EL GPIO pin que usaremos para el led

bool interruptflag = 1; // flag para el interrupt
bool LedStatus = 0; //Led apagado


void setup() {
  
  pinMode(PINHall, INPUT_PULLUP); //Establecemos el GPIO pin 2 como entrada (sensor Hall), el sensor necesita un pull up asi que lo configuramos por software
  pinMode(PINLed, OUTPUT); // Pin para el led
  
  attachInterrupt(digitalPinToInterrupt(PINHall), funcionInterrupt, CHANGE); //definimos un interrupt para el sensor hall
}

void loop() {
  // Una simple escala DO-RE-MI
  
  if(interruptflag==1)
  {
    tone(PinBuzzer,DO,250);
    delay(300); // Agregamos un pequeno retraso entre notas para poder distinguir los cambios entre tonos
    tone(PinBuzzer,RE,250);
    delay(300);
    tone(PinBuzzer,MI,250);
    delay(300);
  }
  else
  {
    LedStatus = !LedStatus;
    digitalWrite(PINLed, LedStatus); //Mandamos un 1 logico a la salida

    interruptflag = 1;
  }
}



void funcionInterrupt() { 
    interruptflag = 0;
}
