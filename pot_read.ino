#define x A0
int b1 = 8;

void setup(){
  pinMode(x, INPUT);
  pinMode(b1, INPUT);
  Serial.begin(9600);
}

void loop(){
  if (digitalRead(b1)==HIGH){
    Serial.println(-1);
    delay(500);
  } else {
    Serial.println(analogRead(x));
  }
 
}
