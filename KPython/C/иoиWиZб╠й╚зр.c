#include <stdio.h>
 int main()
{
  char a[12]="hello world";
  int i=0,j=10;
  char tmp;
  while (i<j)
  {
    tmp= a[i];
    a[i]=a[j];
    a[j]=tmp;
    i++;j--;
  }

  printf("%s\n",a);
  return 0;
}

// printf("%c",a)  for循环不改变原定义
// printf("%s",a)  直接输出字符串
//
