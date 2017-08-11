#include <stdio.h>
int main ()
{
  int a[3][4]={2,3,9,5,6,7,8,3,0,5,7,5};
  int i,j,k,x,y,z=0;
  printf("数组 a: \n");
  for(i=0;i<3;i++)
  {
    for(j=0;j<4;j++)
      printf("%2d",a[i][j]);
    printf("\n");
  }
  for(i=0;i<3;i++)
  {
    y=0;
    for(j=1;j<4;j++)
      if(a[i][j]>a[i][y])
      y=j;
    k=1;
    for(x=0;x<4;x++)
      if(a[x][y]<a[i][y])
        k=0;
    if(k!=0)
    {
      printf("鞍点 a[%d][%d]=%d\n",i,y,a[i][y]);
      z=1;
    }
  }
  if(z!=1)
    printf("无鞍点\n");
  return 0;
}
