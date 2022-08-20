#include <ArduinoJson.h>
#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
int buzzer = 10;
int smokeA0 = A5;
// Your threshold value
int sensorThres = 250;


void setup() {
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);
 // Serial.println(F("DHTxx test!"));
  Serial.begin(9600);
  dht.begin();
}

void loop() {
 
  int analogSensor = analogRead(smokeA0);
  float t = dht.readTemperature();
  Serial.print(t);


  Serial.print("X");
  Serial.println(analogSensor);
  // Checks if it has reached the threshold value
//  if (analogSensor > sensorThres and t>35)
//  {
//    tone(buzzer, 1000, 200);
//  }
//  else
//  {
//    noTone(buzzer);
//  }
 delay(300);
}
