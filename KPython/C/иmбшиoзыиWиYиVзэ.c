#include <stdio.h>
int main ()
{
  int a[2][3]={1,2,3,4,5,6};
  int (*p)[3]=a;
  // int (*p)[4]=a;
  printf("%d\n",*p[1]);
// printf("%d\n",p[1][1]);
}
