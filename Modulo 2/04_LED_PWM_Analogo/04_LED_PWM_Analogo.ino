
int PINout = 2; // EL GPIO pin que usaremos para el led


void setup() 
{
  pinMode(PINout, OUTPUT); //Establecemos el GPIO pin 2 como salida analoga
}


// La funcion loop corre infinitamente
void loop() 
  {
    /* 
      La resolucion del PWM del ESP8266 es de 10 bits, 
      asi que el valor de salida debe de estar entre
      un valor de 0 y 1023
    */
  
    //brillo al 0%
    analogWrite(PINout, 0);
    delay(500);

    //brillo al 25%
    analogWrite(PINout, 255);
    delay(500);

    //brillo al 50%
    analogWrite(PINout, 512);
    delay(500);

    //brillo al 75%
    analogWrite(PINout, 768);
    delay(500);

    //brillo al 100%
    analogWrite(PINout, 1023);
    delay(500);

    

  
  
  }
