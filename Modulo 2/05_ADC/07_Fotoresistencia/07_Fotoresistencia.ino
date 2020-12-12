
const int PINADC = A0; // El pin A0 usado para ADC
const int PINout = 2; // EL GPIO pin que usaremos para el led


int Lectura = 0; //lectura obtenida del divisor del voltage de la fotoresistencia

void setup()
{
  Serial.begin(9600); // Inicializamos el puerto serial y especificamos los baudios
  pinMode(PINout, OUTPUT); //Establecemos el GPIO pin 2 como salida analoga
}

// La funcion loop corre infinitamente
void loop()
{
  /*
    La resolucion del ADC del ESP8266 es de 10 bits,
    asi que el valor de salida
    debe de estar entre un valor de 0 y 1023
  */

  //leemos del pin ADC
  Lectura = analogRead(PINADC);
  if (Lectura > 150) // Establecemos un valor a prueba y error
  {
    digitalWrite(PINout, HIGH); // por debajo del limite el led permanece apagado
  } else
  {
    digitalWrite(PINout, LOW); // arriba del limite el led se enciende (oscuridad)
  }

  //Escribimos el resultado en el puerto serial, ideal para debuggear codigo
  Serial.print("Lectura fotoresistencia: ");
  Serial.println(Lectura);

  delay(500); //un retraso unicamente para propositos de ejemplo, para poder leer la data en el monitor serial apropiadamente
}
