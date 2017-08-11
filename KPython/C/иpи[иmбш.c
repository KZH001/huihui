#include <stdio.h>
int main()
{
  int a,b=0;
  scanf("%d",&a);
  if(a==0)
  {printf("1\n");}
  else{
  while(a>0)
{
  b++;a/=10;
}
  printf("%d\n",b);
}
return 0;
}
