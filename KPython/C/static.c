#include <stdio.h>
int fun ()
{
  // static
  int a=3;
  a++;

  return a;
}
int main ()
{
  printf("%d\n",fun());
  printf("%d\n",fun());
  printf("%d\n",fun());
  return 0;
}
