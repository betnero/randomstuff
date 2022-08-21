#include <Mouse.h>

void setup() {
delay(2000);
Serial.begin(9600);
Mouse.begin();
}

void loop() {
Mouse.move(-3,0);
delay(5);
Mouse.move(3,0); 
delay(290000);
}
