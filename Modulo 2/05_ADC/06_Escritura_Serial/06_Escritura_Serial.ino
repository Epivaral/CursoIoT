
const int PINADC = A0; // El pin A0 usado para ADC


int Lectura =0; //lectura obtenida del potenciometro

void setup() 
{
  Serial.begin(9600); // Inicializamos el puerto serial y especificamos los baudios
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

    //Escribimos el resultado en el puerto serial, ideal para debuggear codigo
    Serial.print("Lectura ADC: ");
    Serial.println(Lectura);
    
    delay(500); //un retraso unicamente para propositos de ejemplo, para poder leer la data en el monitor serial apropiadamente
  }
