#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial2.begin(9600);
}

void loop() {
  // read from port 1, send to port 0:

  if (Serial2.available()) {

    int inByte = Serial2.read();

    Serial.write(inByte);

  }

  // read from port 0, send to port 1:

  if (Serial.available()) {

    int inByte = Serial.read();
    Serial.write(inByte);
    Serial2.write(inByte);

  }

}