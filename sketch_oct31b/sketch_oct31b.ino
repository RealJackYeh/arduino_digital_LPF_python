void setup() {
  Serial.begin(115200);
}
float xn1 = 0; // = x[n-1]
float yn1 = 0; // = y[n-1]
int k = 0;

void loop() {
  float t = micros()/1.0e6;
  float xn = sin(2*PI*2*t) + 0.2*sin(2*PI*15*t);
  float yn = 0.939*yn1 + 0.0304*xn + 0.0304*xn1; // y[n] = 0.939*y[n-1] + 0.0304*x[n] + 0.0304*x[n-1]
  delay(1);  // to make loop() speed 1kHz
  xn1 = xn;
  yn1 = yn;
  if (k % 3 == 0) {
    Serial.print(xn);
    Serial.print(" ");
    Serial.println(yn);   
  }
  k = k+1;
}
