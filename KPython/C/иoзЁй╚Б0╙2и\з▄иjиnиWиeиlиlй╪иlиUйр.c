#include <stdio.h>
int main ()
{
  int i,j,k,x=0,y=0;
  int a[3][4]={{1,2,3,4},{9,8,7,6},{-10,10,-5,2}};
  k=a[0][0];
  for(i=0;i<=2;i++)
  for(j=0;j<=3;j++)
  if(a[i][j]>k)
  {
    k=a[i][j];
    x=i;y=j;
  }
  printf("k=%d,x=%d,y=%d\n",k,x,y);
return 0;
}
