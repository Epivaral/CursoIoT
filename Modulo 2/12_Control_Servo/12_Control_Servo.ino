// Para controlar el Servo, usamos la libreria Servo.h incluida en el instalador del Arduino IDE
#include <Servo.h>

Servo servo1;  // Definimos el objecto Servo

const int PinServo = D1; //GPIO que usaremos para controlar el servo
const int PINADC = A0; // El pin A0 usado para ADC

int Lectura =0; //lectura obtenida del potenciometro


void setup() {
  servo1.attach(PinServo);  // Inicializamos el objeto Servo en el pin elegido
  servo1.write(0); //ponemos el servo en la posicion 0

  Serial.begin(9600);
}

void loop() {
  
  int posLectura =0; //la posicion que leeremos del servo.
  
  Lectura = 0.175 * analogRead(PINADC); // convertimos de 0 a 1024 (ADC) a 0 a 180 (grados) por regla de tres
  
  servo1.write(Lectura); //colocamos el servo en la posicion aleatoria
  
  posLectura = servo1.read(); // Leemos la posicion actual del servo

  //Desplegamos la posicion obtenida (en grados)
  Serial.print("Posicion actual: ");
  Serial.print(posLectura);
  Serial.println(" Grados");

  delay(200);
  
}
