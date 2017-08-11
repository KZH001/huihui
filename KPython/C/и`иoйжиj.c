#include <stdio.h>
int main ()
{
  int sum=0;
  int a=1,b;
  for(a=1;a<=10;a++)
  {
    int c=1;
    for(b=a;b>0;b--)
    {
      c*=b;
    }
    sum+=c;
  }
  printf("%d\n",sum);
  return 0;
}

#include <stdio.h>
int main ()
{
  int a,b=1;
  int c=0;
  for(a=1;a<=5;a++)
  {
    b*=a;c+=b;
  }
  printf("%d\n",c);
  return 0;
}
