#define x A0

void setup(){
  pinMode(x, INPUT);
  Serial.begin(9600);
}

void loop(){
  Serial.println(analogRead(x));
 
}
