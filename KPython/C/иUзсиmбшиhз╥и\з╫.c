#include <stdio.h>
void xz(int a[],int n)
{
  int i,j,k,x;
  for(i=0;i<n-1;i++)
  {
    k=i;
    for(j=i+1;j<n;j++)
    {
      if(a[k]>a[j])
      {
        k=j;
      }
    }
    if(i!=k)
    {x=a[i];
      a[i]=a[k];
      a[k]=x;
    }
  }
}
int main(int argc, char const *argv[])
{
  int a[8]={2,4,6,7,9,1,3,5};
  xz(a,8);
  for(int i=0;i<8;i++)
  {
    printf("%d",a[i]);
  }
  printf("\n");
  return 0;
}
