#include <Servo.h>

// Pinos
const int signalPin = 2;
const int servoPin = 9;
const int ledGreenPin = 3;
const int ledRedPin = 4;
const int irSensorPin = 5;

// Objeto Servo
Servo myServo;

// Estado do sinal
bool signalState = false;
unsigned long previousMillis = 0;
const long interval = 10000; // Intervalo de 10 segundos

void setup() {
  pinMode(signalPin, INPUT);
  pinMode(ledGreenPin, OUTPUT);
  pinMode(ledRedPin, OUTPUT);
  pinMode(irSensorPin, INPUT);

  myServo.attach(servoPin);
  myServo.write(0); // Posição inicial do servo
}

void loop() {
  signalState = digitalRead(signalPin);

  if (signalState == HIGH) {
    myServo.write(90); // Move o servo para 90 graus
    digitalWrite(ledGreenPin, HIGH); // Acende a luz verde
    digitalWrite(ledRedPin, LOW); // Apaga a luz vermelha

    // Verifica o sensor infravermelho a cada 10 segundos
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;

      int irState = digitalRead(irSensorPin);
      if (irState == LOW) { // Objeto detectado
        // Não volta o servo ao estado anterior
        delay(interval); // Espera mais 10 segundos
      } else {
        myServo.write(0); // Volta o servo à posição inicial
      }
    }
  } else {
    myServo.write(0); // Servo não se move
    digitalWrite(ledGreenPin, LOW); // Apaga a luz verde
    digitalWrite(ledRedPin, HIGH); // Acende a luz vermelha
  }
}
