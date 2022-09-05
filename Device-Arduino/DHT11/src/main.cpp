#include <Arduino.h>
#include "DHT.h"  
          
const int DHTPIN = 4;      
const int DHTTYPE = DHT11; 
const unsigned long TIME_UNIX = 1662337229L + 3600L;

DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  dht.begin();       
}

void loop() {
  unsigned long timeNow = TIME_UNIX + millis()/1000;
  float humidity = dht.readHumidity();    
  float temp = dht.readTemperature(); 

  Serial.print(temp);               
  Serial.print(" ");
  Serial.print(humidity);
  Serial.print(" ");
  Serial.println(timeNow);         
  delay(1000);                   
}
