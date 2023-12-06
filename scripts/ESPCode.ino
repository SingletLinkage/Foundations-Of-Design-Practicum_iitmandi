/**
@author: Arka B23120
*/

#include <ESP8266WiFi.h>
#include <ESPAsyncWebSrv.h>
#include <math.h>

const char *ssid = "_void>"; // put wifi name here
const char *password = "<your pwd>"; //put wifi pwd here
int x=0, y=0;

#define echo1 D8
#define trig1 D7
#define echo2 D6
#define trig2 D5

#define en12 D1
#define in1 D2
#define in2 D3
#define in3 D2
#define in4 D3
#define en34 D4

// the above defined are pins for esp8266; you can use GPIO notation too
// due to the lack of pins, we are using same pin for in1 and in3; same for in2 and in4
// not an issue since all wheels rotate in the same direction in this code

long duration; // in ms
long duration_side;
float front_distance;
float side_distance;
float msTocm = 0.017;

float theta = 0;
float thetapersec = 27; //degrees
float vel = 5;

int right_c = 0, left_c = 0; 
// counters for filtering out random left/right turns; this is VERY important if you want to have somewhat accurate theta

long t1,t2;

AsyncWebServer server(80);

void setup() {
  Serial.begin(9600);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(en12, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(en34, OUTPUT);
  pinMode(trig1, OUTPUT);
  pinMode(echo1, INPUT);
  pinMode(trig2, OUTPUT);
  pinMode(echo2, INPUT);

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);  
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  wifi_init();
  forward();
}

void wifi_init(){
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Obtain and print the local IP address
  IPAddress ip = WiFi.localIP();
  Serial.println("***************************************");
  Serial.print("IP Address: ");
  Serial.println(ip);
  Serial.println("***************************************");

  // Define server routes -> send the putput of fetch() with status code 200 each time server receives a request
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->send(200, "text/plain", fetch());
  });

  // Start server
  server.begin();
}

String fetch(){
  String txt = String(x)+" "+String(y)+ " "+String(theta);
  return txt;
}

float getFrontDist() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig1, LOW);
  delay(2);
  digitalWrite(trig1, HIGH);
  delay(5);
  digitalWrite(trig1, LOW);

  duration = pulseIn(echo1, HIGH);
  front_distance = duration * msTocm;
  //Serial.print("Front: ");
  //Serial.println(front_distance);
  return abs(front_distance);
}

float getSideDist() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig2, LOW);
  delay(2);
  digitalWrite(trig2, HIGH);
  delay(5);
  digitalWrite(trig2, LOW);

  duration = pulseIn(echo2, HIGH);
  side_distance = duration * msTocm;
  //Serial.print("Side: ");
  //Serial.println(side_distance);
  return abs(side_distance);
}

void forward(){
  right_c = 0;
  left_c = 0;
  analogWrite(en12, 255);
  analogWrite(en34, 250);
  // different values of enA and enB since our motors had different speeds at full power -> it was turning to a side insteadd of going forward
  // adjust values until it moves straight
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  t1 = millis();
  x += vel*cos(theta * 3.14 / 360);
  y += vel*sin(theta * 3.14 / 360);
  //digitalWrite(in3, HIGH);
  //digitalWrite(in4, LOW);
}

void stop(){
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  //digitalWrite(in3, LOW);
  //digitalWrite(in4, LOW);
}

void right(){
  right_c += 1;
  analogWrite(en12, 170);
  analogWrite(en34, 255);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  t2 = millis();
  if (right_c > 2)  theta += thetapersec * (t2 - t1) / 1000;
  t1 = t2;
  //digitalWrite(in3, HIGH);
  //digitalWrite(in4, LOW);
}

void left(){
  left_c += 1;
  analogWrite(en12, 255);
  analogWrite(en34, 170);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  t2 = millis();
  if (left_c > 2) theta -= thetapersec * ((t2 - t1) / 1000);
  t1 = t2;
  //digitalWrite(in3, HIGH);
  //digitalWrite(in4, LOW);
}

void loop(){
  if (theta > 360){
    stop();
    Serial.println("ACHIEVED");
  } 
  // setup threshold distances based on requirements
  else if (getFrontDist() >= 15){
    float side = getSideDist();
    if (side >= 10){
      right();
      Serial.println("RIGHT");
    }else if (side <= 5){
      left();
      Serial.println("LEFT");
    }else{
      Serial.println("FORWARD");
      forward();
    }
  }else{
    Serial.println("STOP");
    stop();
  }
  Serial.println(String(x) + " " + String(y));
  delay(20);
}
