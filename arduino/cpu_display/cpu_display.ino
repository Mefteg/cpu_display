/**
 * Display the received value (an integer between 0 and 255)
 * through a 1mA AmpMeter connected to pin 10 (using PWM).
 * Print back the received value.
 */
 
#define PIN 10

#define BAUDRATE 9600

int cpu = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(PIN, OUTPUT);

  Serial.begin(BAUDRATE);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    cpu = Serial.parseInt();

    if (cpu < 0 || cpu > 255)
    {
      cpu = 255;
    }

    String str(cpu); // convert int to String
    Serial.println(str);
  }

  analogWrite(PIN, cpu);

  delay(10);
}
