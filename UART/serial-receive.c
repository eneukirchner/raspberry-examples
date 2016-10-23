#include <stdio.h>
#include <string.h>
#include <errno.h>

#include <wiringPi.h>
#include <wiringSerial.h>

int main ()
{
  int fd ;
  int count ;
  unsigned int nextTime ;
  int c;

  if ((fd = serialOpen ("/dev/ttyS0", 115200)) < 0) {
    fprintf (stderr, "Unable to open serial device: %s\n", strerror (errno)) ;
    return 1 ;
  }

  if (wiringPiSetup () == -1) {
    fprintf (stdout, "Unable to start wiringPi: %s\n", strerror (errno)) ;
    return 1 ;
  }

  for (;;) {
    c = serialGetchar (fd);
    if (c > 0) {
    	putchar(c) ;
    }
    fflush (stdout) ;
  }

  return 0 ;
}
