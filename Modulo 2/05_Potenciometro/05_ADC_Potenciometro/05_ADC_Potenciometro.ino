
const int PINADC = A0; // El pin A0 usado para ADC
const int PINout = 4; // El Pin para el led que usaremos

int Lectura =0; //lectura obtenida del potenciometro

void setup() 
{
  pinMode(PINout, OUTPUT); //Establecemos el GPIO pin 4 como salida analoga
}


// La funcion loop corre infinitamente
void loop() 
  {
    /* 
      La resolucion del ADC del ESP8266 es de 10 bits,
      al igual que el PWM, asi que el valor de salida 
      debe de estar entre un valor de 0 y 1023
    */
    Lectura = analogRead(PINADC);
    analogWrite(PINout, Lectura);
    
  }
