#include <stdio.h>
int main ()
{
  int a[10];
  int *p,i;
  p=a;
  for(i=0;i<10;i++)
  scanf("%d",p++);
  printf("\n");
  p=a;
  for(i=0;i<10;i++,p++)
  printf("%d",*p);
  printf("\n");
  return 0;

}
