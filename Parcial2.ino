const int bred = A0;
const int bama = A1;
const int pote = A2;
const int red = 9;
const int ama = 8;
int voltaje = 0;
int voltajeB = 0;
int sensorvalue = 0; // Variable para almacenar el valor del potenciometro
int bstatered = 0;
int bstateama = 0;
 
void setup() {
  pinMode(red, OUTPUT);
  pinMode(ama, OUTPUT);
  pinMode(bred, INPUT);
  pinMode(bama, INPUT);
  Serial.begin(9600);
}
 
void loop(){
  bstatered = digitalRead(bred);
  bstateama = digitalRead(bama);

  if (bstatered == HIGH) {
    sensorvalue = analogRead(pote);
    voltaje = sensorvalue/4;
    analogWrite(red,voltaje); //Los valores de analogRead van de 0 a 1023, los de analogWrite de 0 a 255
    Serial.println(voltaje);
  }else if(bstateama == HIGH){
    sensorvalue = analogRead(pote);
    voltajeB = sensorvalue/4;
    analogWrite(ama, voltajeB);
    Serial.println(voltajeB);
  }else {
    digitalWrite(red, LOW);
    digitalWrite(ama, LOW);
   }
 }
