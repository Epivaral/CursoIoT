const int TRIG_PIN = 5; //D1 - GPIO5 que manda el pulso al sensor
const int ECHO_PIN = 4; //D2 - GPIO4 que recibe el pulso del sensor

// una distancia mayor de 400 cm (23200 us) esta fuera de rango
const unsigned int MAX_DIST = 23200;

void setup() {

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT); 
  
  digitalWrite(TRIG_PIN, LOW); //Inicializamos los pines

  // usaremos el monitor serial para obtener las lecturas
  Serial.begin(9600);
}

void loop() {
  unsigned long ancho_pulso;
  float cm;

  // mandamos un pulso por 10 milisegundos
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // esperamos a que el pulso regrese
  ancho_pulso = pulseIn(ECHO_PIN, HIGH);


  cm = ancho_pulso / 58.0; //C*2 = 58.0  (C = 29.1 cm/us)


  if ( ancho_pulso < MAX_DIST )
  {
    Serial.print(cm);
    Serial.println(" cm");
  } else
  {
    Serial.println("Fuera de Rango");
  }

  // esperamos 500 milisegundos para la proxima lectura
  delay(500);
}
