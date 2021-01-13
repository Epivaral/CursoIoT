//Libreria para controlar el Motor Driver TB6612FNG
// Disponible en: https://github.com/sparkfun/SparkFun_TB6612FNG_Arduino_Library

#include <SparkFun_TB6612.h>

#define AIN1 4
#define AIN2 5
#define PWMA 13

const int PinIN = 2;

//Inicializamos el motor (este driver puede manejar 2 motores simultaneamente, pero en este ejemplo solo usaremos uno)
Motor motor1 = Motor(AIN1, AIN2, PWMA, 1, -1); 

void setup() {
  motor1.brake(); //inicializamos con el motor detenido
  pinMode(PinIN, INPUT_PULLUP);
}

int Lectura =0; //lectura obtenida del potenciometro

bool Estado = 0; // Tomado de nuestro circuito #3 03_Toggle_and_delay_Push_Button_y_LED
bool EstadoInterno = 1;


void loop() {

  Lectura = analogRead(A0); // Potenciometro para controlar la velocidad

  Estado = digitalRead(PinIN);
  if (Estado == LOW)
    {
      EstadoInterno = !EstadoInterno;
      delay (200); // un retardo de 200 milisegundos luego de cambiar el estado para evitar el efecto rebote
    }

    //Ponemos una duracion corta, para que el efecto de cualquier cambio sea casi inmediato
    
  if(EstadoInterno==0)
    {
      motor1.drive(Lectura,10); // El primer argumento es la velocidad desde -1024 a 1024, el segundo argumento es la duracion en milisegundos
    }
  else
    {
      motor1.drive(Lectura*-1,10); // velocidad negativa (el motor gira hacia el lado contrario)
    }            

  
}
