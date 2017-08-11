#include <stdio.h>
int main()
{
  int a,b,c;
  for(a=1;a<1000;a++)
  {
    c=0;
    for(b=1;b<a;b++)
    {
      if(a%b==0)
      {
        c+=b;
      }
    }
      if(a==c)
      {
        printf("%d\n",c);
      }
    }
    return 0;
}
