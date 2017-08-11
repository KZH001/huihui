#include <stdio.h>
int main ()
{
  int a;
  int b[10]={1,1};
  for(a=2;a<10;a++)
  {
    b[a]=b[a-2]+b[a-1];
  }
  for(a=0;a<10;a++)
  {
    if(a%5==0)

      printf("\n");
      printf("%5d",b[a]);

  }
  printf("\n");
  return 0;
}
