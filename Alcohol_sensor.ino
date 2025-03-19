  int red = 10; //Set red LED to pin 10
  int yellow = 9; //Set yellow LED to pin 9
  int green = 8; //Set green LED to pin 8
  int buzzer = 11; //Set buzzer to pin 11
void setup()
{
  Serial.begin(9600); //Set serial baud rate to 9600 bps
  pinMode (red, OUTPUT); //Set red LED to output mode so we can control it
  pinMode (yellow, OUTPUT); //Set yellow LED to output mode so we can control it
  pinMode (green, OUTPUT); //Set green LED to output mode so we can control it
  pinMode (buzzer, OUTPUT); //Set buzzer to output mode so we can control it
}
void loop()
{
int val; //Creates "val" value for the alcohol sensor
val=analogRead(0);//Read Gas value from analog 0
Serial.println(val,DEC);//Print the value to serial port
delay(100);//Device reads value from the alcohol sensor every 100 milliseconds
if (val < 120) { //if value from the alcohol sensor is lower than 120 (no alcohol in blood), the green LED turns on
  digitalWrite(green, HIGH);
  digitalWrite(yellow, LOW);
  digitalWrite(red, LOW);
  noTone(buzzer);
}
else if (val >= 120 and val <= 400){//if the value from the alcohol sensor is higher than or equal to 120 and lower than or equal to 400 (some alcohol in blood), the yellow LED turns on and it stays on for 1000 milliseconds
  digitalWrite(yellow, HIGH);
  digitalWrite(green, LOW);
  digitalWrite(red, LOW);
  noTone(buzzer);
  delay(1000);
}
else if (val > 400){//if the value from the alcohol sensor is higher than 400 (a lot of alcohol in blood), the red LED turns on and buzzer starts to play a tone
  digitalWrite(red, HIGH);
  digitalWrite(yellow, LOW);
  digitalWrite(green, LOW);
  tone(buzzer, 1000);
  delay(600);
  noTone(buzzer);
  delay(600);
  tone(buzzer, 1000);
  delay(600);
  noTone(buzzer);
  delay(600);
}
}