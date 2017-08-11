#include <stdio.h>
int main ()
{
  int a[8]={4,5,6,8,1,3,2,9};
  int i,j,k;
  for(i=1;i<8;i++)
  {
    k=a[i];
    j=i-1;
    while(j>=0&&k<a[j])
    {
      a[j+1]=a[j];
      j--;
    }
    a[j+1]=k;
  }
  for(i=0;i<8;i++)
  printf("%d",a[i]);
  printf("\n");
  return 0;
}
