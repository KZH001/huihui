#include <stdio.h>
int main ()
{
  int a[8]={2,5,4,6,7,8,9,3};
  int i,j,k;
  for(i=0;i<8-1;i++)
  {
    for(j=0;j<8-i-1;j++)
    {
      if(a[j]>a[j+1])
      {
        k=a[j];
        a[j]=a[j+1];
        a[j+1]=k;
      }
    }
  }
  for(i=0;i<8;i++)
  {
    printf("%d",a[i]);
  }
  printf("\n");
  return 0;
}
