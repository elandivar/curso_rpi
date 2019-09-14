// Yubox Companion
// Prueba conexión WiFi
// Created by: Edgar Landivar
// Usted es libre de copiar y distribuir
// www.yubox.com

#include <WiFi.h>

const char* ssid       = "XXXXX";
const char* password   = "XXXXX";

void setup() {
  Serial.begin(115200);
  connectToNetwork();
}


void loop() { 
}

void connectToNetwork() {
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Estableciendo conexión con la red WiFi..");
  }
  Serial.println("Conectado!!!");
}
