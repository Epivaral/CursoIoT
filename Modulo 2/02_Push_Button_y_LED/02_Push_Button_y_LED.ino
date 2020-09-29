const int PINout = 4; //El GPIO pin que usaremos para el led
const int PINin = 5; //EL GPIO pin que usaremos para el push button

void setup() {
  pinMode(PINin, INPUT_PULLUP); //Establecemos el GPIO pin 5 como entrada
  pinMode(PINout, OUTPUT); //Establecemos el GPIO pin 4 como salida
}

// La funcion loop corre infinitamente
bool Estado = 0;
void loop() {
  // Leemos constamentente el estatus del push button, 
  // ya que usamos una configuracion PULL UP, el 0 es cuando presionamos el boton y 1 es cuando lo dejamos de presionar
  Estado = digitalRead(PINin); 
  
  if(Estado==0)
    {
      digitalWrite(PINout, HIGH); //Mandamos un 1 logico a la salida
    }
  else
    {
      digitalWrite(PINout, LOW); //Mandamos un 0 logico a la salida
    }                    
}
