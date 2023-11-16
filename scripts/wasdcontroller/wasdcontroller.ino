#include <ESP8266WiFi.h>
#include <ESPAsyncWebSrv.h>

const char *ssid = "_void>"; // put wifi name here
const char *password = "arka2004";
const int yvel = 2;
const int xvel = 2;
const int DIST_THRESHOLD = 25l;

// default values are supposed to change, these are random values currently
int x_0 = 200, y_0 = 200;
int x = 200;
int y = 200;
int dist = 0;

AsyncWebServer server(80);

void setup() {
  Serial.begin(9600);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Obtain and print the local IP address
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // Define server routes
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request) {
    request->send(200, "text/plain", fetch());
  });

  // Start server
  server.begin();
}

void forward(){
  dist += yvel;
  y = y-yvel;
}
void back(){
  dist += yvel;
  y = y+yvel;
}
void right(){
  x += xvel;
}
void left(){
  x -= xvel;
}

void loop() {
  // Append a random number to the array every second
  if (is_running()){
    char key = Serial.read();
    if (key != -1){
      key = char(tolower(key));
      switch(key){
        case 'w':
          forward();
          break;
        case 'a':
          left();
          break;
        case 's':
          back();
          break;
        case 'd':
          right();
          break;
      }
    }
  }
  Serial.println(fetch());
  delay(500);  // Adjust the delay as needed
}

bool is_running(){
  int disp = (x-x_0)*(x-x_0) + (y-y_0)*(y-y_0);
  if ((disp <= DIST_THRESHOLD) && (dist > DIST_THRESHOLD)){
    return false;
  }else{
    return true;
  }
}

String fetch(){
  String txt = "("+String(x)+", "+String(y)+")";
  return txt;
}