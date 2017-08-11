#include <stdio.h>
int h(int a,int b)
{
  int c;
  c=a+b;
  return c;
}

int main()
{
  int i;
  i=h(1,2);
  printf("%d\n",i);
  return 0;
}
