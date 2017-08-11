#include <stdio.h>
int fun (int n);
void main()
{
  printf("%d\n",fun(10));
}
int fun(int n)
{
  int t=1;
  if(n>0)
  t=n*fun(n-1);
  return t;
}

#include <stdio.h>
int kkk(int kk);
void main ()
{
  printf("%d\n",kkk(10));
}
int kkk(int kk)
{
  int k=1;
  if(kk>0)
  k=kk*kkk(kk-1);
  return k;
}
