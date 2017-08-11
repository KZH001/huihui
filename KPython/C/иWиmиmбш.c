#include <stdio.h>
int main()
{
  int a,b;
  int flag=0;
  for(a=2;a<=100;a++)
  {
    flag=0;
    for(b=2;b<=a/2;b++)
    {
      if(a%b==0)
      {
        flag=1;break;
      }
    }
    if(flag==0)
    {
      printf("%d ",a);
    }
  }
  printf("\n");
  return 0;
}
