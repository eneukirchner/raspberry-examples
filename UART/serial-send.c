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
  char* text = "Hallo BULME 2016";
  char c;
  int i = 0;

  if ((fd = serialOpen ("/dev/ttyS0", 115200)) < 0)
  {
    fprintf (stderr, "Unable to open serial device: %s\n", strerror (errno)) ;
    return 1 ;
  }

  if (wiringPiSetup () == -1)
  {
    fprintf (stdout, "Unable to start wiringPi: %s\n", strerror (errno)) ;
    return 1 ;
  }


  while ((c = *(text++))) {  
      printf ("Out: %c\n", c) ;
      fflush (stdout) ;
      serialPutchar (fd, c) ;
      delay(1);
 }

  printf ("Fertig\n") ;
  return 0 ;
}
