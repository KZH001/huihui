#include <stdio.h>
int main()
{
  int a,b,c,d;
  printf("100-999的水仙花数 \n");
  for(d=100;d<999;d++)
  {
    a=d/100;
    b=d/10%10;
    c=d%10;
    if(d==a*a*a+b*b*b+c*c*c)
    printf("%d \n",d);
  }
  return 0;
}
