#include <stdio.h>
int main ()
{
  int a[3][4]={{5,4,6,},{'0',6,4,6},{6,1,2,}};
  int i,j;
  for(i=0;i<3;i++)
  {
    for(j=0;j<4;j++)
    {
      printf("%d",a[i][j]);
    }
    printf("\n");
  }
  return 0;
}
