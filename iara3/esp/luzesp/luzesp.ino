#include <ESP8266WiFi.h>
#include <Wire.h>

const char *ssid = "Comunavirus";
const char *password = "MestreMacaco2020";

IPAddress server(192,168,1,9);       // the fix IP address of the server
WiFiClient client;

// Set your Static IP address
IPAddress local_IP(192, 168, 1, 5);
// Set your Gateway IP address
IPAddress gateway(192, 168, 1, 1);

IPAddress subnet(255, 255, 255, 0);
IPAddress primaryDNS(198, 162, 1, 1);   //optional
IPAddress secondaryDNS(8, 8, 8, 8); //optional

void setup() {
  Serial.begin(115200);
  delay(10);

  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
    Serial.println("STA Failed to configure");
  }

  conectar_wifi();
  print_conexao_wifi();
  

  pinMode(14, OUTPUT);
}

void loop() {
  conectar_server();
  
  String answer = receber();
  
  Serial.println("from server: " + answer);
  client.flush();
  if (answer == "1") {
    digitalWrite(14, HIGH);
  } else if (answer == "0") {
    digitalWrite(14, LOW);
  }
}

void enviar(){
  client.println("birl Hello server! Are you sleeping?\r");
  Serial.println("Enviado ao servidor");
}

String receber(){
  String answer = client.readStringUntil('\r');
  Serial.println("Recebido do servidor");
  return answer;
}

void conectar_wifi(){
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
}

void print_conexao_wifi(){
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void conectar_server(){
  Serial.print("Conectando ao servidor");
  while (!client.connect(server, 8080)){
    Serial.print(".");
  }
}
