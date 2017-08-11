#include <stdio.h>
int main ()
{
  int a[4][4]={{2,4,5},{5,4,6},{8,2,4}};
  int i,j;
  for(i=0;i<4;i++)
  {
    for(j=0;j<4;j++)
    {
      printf("%d",a[i][j]);
    }
    printf("\n");
  }
  return 0;
}
