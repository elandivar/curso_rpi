// Yubox Companion
// Prueba sensor BMP280 on-board
// Conectado al bus I2C
// Created by: Edgar Landivar
// Usted es libre de copiar y distribuir
// www.yubox.com

#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

#define SEALEVELPRESSURE_HPA (1012.00)

Adafruit_BMP280 bmp; // I2C
unsigned long delayTime;
float temp, pres;

void setup() {
  Serial.begin(115200);
  Serial.println(F("BMP280 test"));

  bool status;
  status = bmp.begin(0x76);  
  if (!status) {
    Serial.println("No se encuentra un sensor BMP280 conectado al bus I2C de Yubox Companion");
    while (1);
  }
    
  delayTime = 1000;
  Serial.println();
}

void loop() { 
  printValues();     
  delay(delayTime);
}

void printValues() {

  temp = (float)bmp.readTemperature();
  pres = (float)(bmp.readPressure() / 100.0F);

  Serial.print("Temperatura = ");
  Serial.print(temp);
  Serial.println(" *C");

  Serial.print("Presion = ");
  Serial.print(pres);
  Serial.println(" hPa");

  Serial.print("Altitud Aprox.  = ");
  Serial.print(bmp.readAltitude(SEALEVELPRESSURE_HPA));
  Serial.println(" m");
  
  Serial.println();
}
