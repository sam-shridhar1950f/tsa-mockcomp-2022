#include "heltec.h"
#define BAND    915E6 

int counter = 0;
#define Open_LED  12
#define Close_LED 13
void setup() {
  
  /
  Heltec.begin(false /*DisplayEnable Enable*/, true /*Heltec.LoRa Disable*/, true /*Serial Enable*/, true /*PABOOST Enable*/, BAND /*long BAND*/);
	pinMode(Open_LED,INPUT);
    digitalWrite(Open_LED,LOW);
	pinMode(Close_LED,INPUT);
    digitalWrite(Close_LED,LOW);
	LoRa.setTxPower(14,RF_PACONFIG_PASELECT_PABOOST);
  
}

void loop() {
	if(digitalRead(Open_LED)){
	  Serial.print("Sending packet: OpenLED\r\n");
	  // send packet
	  LoRa.beginPacket();
	  LoRa.print("OpenLED");
	  LoRa.endPacket();
	  digitalWrite(Open_LED,LOW);                       
	}
	if(digitalRead(Close_LED)){
		Serial.print("Sending packet: CloseLED\r\n");
		// send packet
		LoRa.beginPacket();
		LoRa.print("CloseLED");
		LoRa.endPacket();
		digitalWrite(Close_LED,LOW);  
	}
	delay(1000);  
}