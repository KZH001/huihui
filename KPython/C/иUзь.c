#include <stdio.h>
#define M 1
int main ()
{
  printf("%d\n",M);
  return 0;
}

#include <stdio.h>
#define ONE 1
#define TWO 2
#define THREE ONE+TWO          /*简单的宏的输出*/
int main ()
{
  printf("%d\n",ONE);
  printf("%d\n",TWO);
  printf("%d\n",THREE);
  printf("%d\n",TWO*THREE);
  return 0;
}
