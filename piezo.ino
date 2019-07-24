#define rfTransmitPin 4
#define piezoPin 13

void setup(){
  pinMode(rfTransmitPin, OUTPUT);
  pinMode(piezoPin,INPUT);

//Set the threshold levels
  int threshold= 500;
}
//if the reading is higher than the threshold value, then the LED is turned ON for a Second You can edit to your sepecification
void loop(){
  int reading= analogRead(piezo_Pin);
  if (reading > threshold){
    digitalWrite(rfTransmitPin, HIGH);
  }
  else{
    digitalWrite(rfTransmitPin, LOW
  }
}
