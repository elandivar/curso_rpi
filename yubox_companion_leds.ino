// Yubox Companion
// Prueba LEDs on-board
// Created by: Edgar Landivar
// Usted es libre de copiar y distribuir
// www.yubox.com

#define LED1 5
#define LED2 39

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED1, HIGH);   
  delay(1000);     
  digitalWrite(LED2, HIGH);   
  delay(1000);                     
  digitalWrite(LED1, LOW);  
  delay(1000);             
  digitalWrite(LED2, HIGH);   
  delay(1000);            
}
