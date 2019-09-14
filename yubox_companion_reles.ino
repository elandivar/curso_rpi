// Yubox Companion
// Prueba relés on-board
// Created by: Edgar Landivar
// Usted es libre de copiar y distribuir
// www.yubox.com

#define REL1 35
#define REL2 32
#define REL3 33

void setup() {
  pinMode(REL1, OUTPUT);
  pinMode(REL2, OUTPUT);
  pinMode(REL3, OUTPUT);

}

void loop() {
  // Activo los relés uno a uno
  digitalWrite(REL1, HIGH);   
  delay(1000);                      
  digitalWrite(REL2, HIGH);   
  delay(1000);    
  digitalWrite(REL3, HIGH);   
  delay(1000);    
  
  // Desactivo los relés uno a uno
  digitalWrite(REL1, LOW);    
  delay(1000);       
  digitalWrite(REL2, LOW);    
  delay(1000);          
  digitalWrite(REL3, LOW);    
  delay(1000);          
}
