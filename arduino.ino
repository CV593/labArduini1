int ledPins[] = {3, 4, 5,6};
int numPins = sizeof(ledPins) / sizeof(ledPins[0]);

void setup() {
  for (int i = 0; i < numPins; i++) {
    pinMode(ledPins[i], OUTPUT); 
    digitalWrite(ledPins[i], LOW); 
  }
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    String mensaje = Serial.readStringUntil('\n'); 
    int pin = mensaje.substring(0, mensaje.indexOf(',')).toInt(); 
    int estado = mensaje.substring(mensaje.indexOf(',') + 1).toInt(); 
    if (pin >= 0 && pin < numPins) { 
      digitalWrite(ledPins[pin], estado); 
      if (estado == HIGH) {
        Serial.print("LED en pin ");
        Serial.print(pin);
        Serial.println(" encendido");
      } else {
        Serial.print("LED en pin ");
        Serial.print(pin);
        Serial.println(" apagado");
      }
    } else {
      Serial.println("Pin no válido");
    }
  }
}
