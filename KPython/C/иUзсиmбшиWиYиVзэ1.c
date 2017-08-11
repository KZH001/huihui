/*函数指针*/
#include <stdio.h>
int fun (int a,int b)
{
  return a+b;
}
int main ()
{
  int (*p)(int ,int);
  p=fun;
  printf("%p\n",fun);
  printf("%d\n",p(1,2));
  return 0;
}
/*函数指针数组*/
#include <stdio.h>
int fun1 (int a,int b)
{
  return a+b;
}
int fun2 (int a,int b)
{
  return a-b;
}
int fun3 (int a,int b)
{
  return a*b;
}
int main ()
{
  int (*p[3])(int,int)={fun1,fun2,fun3};

for(int i=0;i<3;i++)
printf("%d\n",p[i](3,2));

  return 0;
}
