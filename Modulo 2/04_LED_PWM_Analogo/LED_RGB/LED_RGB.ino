//Definimos un pin para cada salida del led RGB
int PINoutR = 4; 
int PINoutG = 0; 
int PINoutB = 2; 

void setup() 
{
  pinMode(PINoutR, OUTPUT); 
  pinMode(PINoutG, OUTPUT);
  pinMode(PINoutB, OUTPUT);
}


void loop() 
{
/*
   Escribimos valores aleatorios a cada pin,
   de esta manera obtendremos colores aleatorios en el led RGB
*/
    analogWrite(PINoutR, random(1023));
    analogWrite(PINoutG, random(1023));
    analogWrite(PINoutB, random(1023));
    delay(100);
}
