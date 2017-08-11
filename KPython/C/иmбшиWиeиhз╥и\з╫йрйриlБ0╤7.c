#include <stdio.h>
int main ()
{
  int a [8]={5,4,6,8,9,7,2,3};
  int i,j,k,min;
  for(i=0;i<8-1;i++)
  {
    min=i;
    for(j=i+1;j<8;j++)
    {
      if(a[min]>a[j])
      {
              min=j;
      }
    }
  if(i!=min)
  {
    k=a[i];
    a[i]=a[min];
    a[min]=k;
  }

  }
  for(i=0;i<8;i++)
  {
    printf("%d",a[i]);
  }
  printf("\n");
  return 0;
  }
