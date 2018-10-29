#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

#define PIN_STAT      0
#define PIN_STAT_ON   0
#define PIN_STAT_OFF  1

#define PIN_BUTTON     7
#define PIN_BUTTON_ON  0
#define PIN_BUTTON_OFF 1

int main(){
	int old_button, button, stat;

	wiringPiSetupGpio();

	pinMode(PIN_STAT, INPUT);
	pinMode(PIN_BUTTON, OUTPUT);

	old_button = digitalRead(PIN_BUTTON);
	stat = digitalRead(PIN_STAT);

	while(1) {
		button = digitalRead(PIN_BUTTON);
		if(button != old_button && button == PIN_BUTTON_ON) {
			stat = digitalRead(PIN_STAT);
			digitalWrite(PIN_STAT, !stat);
		}
		old_button = button;
		printf("stat: %d  button: %d \n", stat, button);
		delay(2500);
	}
	return 0;
}









