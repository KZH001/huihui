#include <stdio.h>
int main()
{
  int a,b;
  loop:

  printd(":\n");
  scanf("%d:%d",&a,&b);
  if(a<0||a>23||b<0||b>59)
  {
    printf("错误\n");
    goto loop;
  }
  if(a>12)
  {
    a-=12;
    printf("%d:%d PM\n",a,b);
    return 1;
  }
  printf("%d:%d AM\n",a,b);
  return 0;

}
