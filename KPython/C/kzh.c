#include <stdio.h>
int main ()
{
  int a[3][3]={5,4,3,4,8,5,1,5,4};
  int i,j,k,x,y,z=0;
  printf("鞍点a:\n");
  for(i=0;i<3;i++)
  {
    for(j=0;j<3;j++)
    {  printf("%d",a[i][j]);  }
    printf("\n");
  }
  for(i=0;i<3;i++)
  {   y=0;
    for(j=1;j<3;j++)
    {
    if( a[i][j]>a[i][y]);
      y=j;

    }
    k=1;
    for(x=0;x<3;x++)
    {
      if(a[x][y]>a[i][y])
      {   k=0;break;   }
    }
    if(k!=0)
    {   printf("鞍点a[%d][%d]=%d\n",i,y,a[i][y]); z=1;  }
  }
    if(z!=1)
    {
      printf("无鞍点\n");
    }
    return 0;
}
