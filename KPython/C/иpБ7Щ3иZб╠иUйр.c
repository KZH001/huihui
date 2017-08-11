#include <stdio.h>

int main ()
{
  unsigned long int i=1,j=1;
  while (i<100000)
  {
    j=1;
    while (j<100000)
    {
      j++;
    }
    i++;
  }
  return 0;
}
