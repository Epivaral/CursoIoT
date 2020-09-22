const int PIN = 4; //El GPIO pin que usaremos

void setup() {
 
  pinMode(PIN, OUTPUT); //Establecemos el GPIO pin como salida
}

// La funcion loop corre infinitamente
void loop() {
  digitalWrite(PIN, HIGH); //Mandamos un 1 logico a la salida
  delay(1000);        //Esperamos 1000 milisegundos (1 segundo)            
  digitalWrite(PIN, LOW); //Mandamos un 0 logico a la salida
  delay(1000);                       
}
