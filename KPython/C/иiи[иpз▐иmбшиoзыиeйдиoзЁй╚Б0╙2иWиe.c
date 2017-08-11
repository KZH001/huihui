#include <stdio.h>
int main()
{
  int a[8]={};
  int i,max=0;
  for(i=1;i<8;i++)
  {
    if(a[max]<a[i])
    {
      max=i;
    }
  }
  printf("a[%d]=%d\n",max,a[max]);
  return 0;
}
