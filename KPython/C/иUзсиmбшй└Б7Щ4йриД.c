#include <stdio.h>
void mp(int a[],int n)
{
  int i,j,k;
  for(i=0;i<n-1;i++)
  {
    for(j=0;j<n-i-1;j++)
    {
      if(a[j]>a[j+1])
      {
        k=a[j];
        a[j]=a[j+1];
        a[j+1]=k;
      }
    }
  }
}
int main(int argc, char const *argv[])
{
  int a[8]={2,4,6,7,9,1,3,5};
  mp(a,8);
  for(int i=0;i<8;i++)
  {
    printf("%d",a[i]);
  }
  printf("\n");
  return 0;
}
