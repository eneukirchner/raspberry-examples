
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <math.h>

#include <wiringPi.h>
#include <softPwm.h>

// The OK/Act LED is connected to BCM_GPIO pin 16

#define LED1  1
#define LED2  0

int main ()
{
  int i;

  wiringPiSetup ()  ;

  softPwmCreate (LED1, 0, 100) ;
  softPwmCreate (LED2, 0, 100) ;

  for (;;)
  {
    for (i = 0 ; i <= 100 ; ++i)
    {
      softPwmWrite (LED1, 100-i) ;
      softPwmWrite (LED2, i) ;
      delay (10) ;
    }
    delay (50) ;

    for (i = 100 ; i >= 0 ; --i)
    {
      softPwmWrite (LED1, 100-i) ;
      softPwmWrite (LED2, i) ;
      delay (10) ;
    }
    delay (10) ;
  }

  return 0 ;
}

