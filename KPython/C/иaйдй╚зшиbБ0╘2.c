#include <stdio.h>
// 寄存器变量空间
int main ()
{  //registre
  int i=1,j=1;
  while (i<100000)
  {
    j=1;
    while (j<100000)
    {
      j++;
    }
    i++;
  }
  return 0;
}
