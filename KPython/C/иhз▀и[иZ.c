#include <stdio.h>
int main ()
{
  char a;
  while (1)
  {
    scanf("%c\n",&a);
    getchar ();
    if(a=='b');
    {
      printf("我'y'\n");
      /*continue;*/  break;
    }
    printf("a=%c\n",a);
  }
  return 0;
}
