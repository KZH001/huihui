#include <stdio.h>
int main ()
{   //extern 联合体
  extern int num;
  printf("num=%d\n",num);
  return 0;
}
int num=1;


#include <stdio.h>
#include "联合.c"
int main ()
{
  printf("num =%d\n",num);
  return 0;
}


#include <stdio.h>
#include "联合.c"
union UN{
  char a;
  int b;
  int c;
};
int main ()
{
  union UN u;
  u.a='$';
  u.b=97;   //97的ascii 值
  printf("%c\n",u.a);
  return 0;
}
#if
#else
#endif

#ifdef
#endif

#ifndef
#endif
