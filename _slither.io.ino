void setup() {
  Serial.begin(115200);  // Must match baudrate in Python script
}

int analogPin=A0;
int a;
int tolerance=45;
int baseline=330;
void loop() {
  a=analogRead(analogPin);  // Read from analog input A1
//  Serial.println(a);
  if (a<baseline-tolerance){ 
  Serial.println('A');  // Send 'A' to move right
  }
  else if (a>baseline+tolerance) {
     Serial.println('C');  // Send 'C' to move left
  }
  else if (a>baseline-tolerance && a<baseline+tolerance){ 
    Serial.println('B');  // Send 'B' to stop
  }  
  delay(150); // Allow time to read serial port
}
