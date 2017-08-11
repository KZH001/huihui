/*函数1-9反过来*/
#include <stdio.h>
void px(int x,int *y)
{/*一次循环*/
  int i,j,k;
  for(i=9-x;i<9;i++)
  {
    k=y[i];
    for(j=i-1;j>=0&&k>y[j];j--)
    {y[j+1]=y[j];}
    y[j+1]=k;
  }
  /*二次循环*/
  for(i=1;i<x;i++)
  {
    k=y[i];
    for(j=i-1;j>=0&&k<y[j];j--)
    {y[j+1]=y[j];}
    y[j+1]=k;
  }
}
int main(int argc, char const *argv[])
{
  int a[9]={1,2,3,4,5,6,7,8,9};
  int b,c;
  scanf("%d",&b);
  px(b,a);
  for(c=0;c<9;c++)
  {printf("%d",a[c]);}
  printf("\n");
  return 0;
}
