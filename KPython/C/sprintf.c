#include <stdio.h>
int main ()
{
char str[128] = {0};
  sprintf(str,"select * from xiao where id = %d",1);

  printf("%s\n",str);

  return 0;
}
