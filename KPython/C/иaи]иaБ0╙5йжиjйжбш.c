#include <stdio.h>
int main ()
{
  int a,b,d;
  char c;
  scanf("%d%d%c",&a,&b,&c);
  switch(c)
  {
    case 43:d=a+b;break;
    case 45:d=a-b;break;
    case 42:d=a*b;break;
    case 47:d=a/b;break;
    case 37:d=a%b;break;
    // case '+':d=a+b;break;
    // case '-':d=a-b;break;
    // case '*':d=a*b;break;
    // case '/':d=a/b;break;
    // case '%':d=a%b;break;
  }
  printf("%d\n",d);
  return 0;
}
