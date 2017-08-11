#include <stdio.h>
int main()
{
  int a[3][4]={2,5,4,6,3,8,7,5,4,6,1,5};
  int i,j,max=a[0][0];
  int x,y;
  x=y=0;

  for(i=1;i<3;i++)
  {
    for(j=0;j<4;j++)
    {
      if(a[x][y]<a[i][j])
      {
        max=a[i][j];
        x=i;y=j;
      }
    }
  }
  printf("a[%d][%d]=%d\n",x,y,max);
  return 0;
}
