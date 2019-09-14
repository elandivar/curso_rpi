 // Yubox Companion
// Prueba switches pulsadores y led
// Created by: Edgar Landivar
// Usted es libre de copiar y distribuir
// www.yubox.com

#define PULS1 25
#define LED 5

void setup() {

  pinMode(PULS, INPUT);
  pinMode(LED, OUTPUT);
  
  Serial.begin(115200);
}

void loop() { 
  if (digitalRead(PULS1) == LOW) {       
    digitalWrite(LED, HIGH);
    Serial.println("Aplastado"); 
    delay(500);
  } else {
    digitalWrite(LED, LOW);
    Serial.println("NO Aplastado"); 
  }
