#include <stdio.h>
int main ()
{
  char a[10]="hello";
  int i=0,j=0;
  char b;
  while (a[j]!='\0')
  j++;j-=1;
  printf("j=%d\n",j);
  while (i<j)
  {
    b=a[i];
    a[i]=a[j];
    a[j]=b;
    i++;j--;
  }
  printf("%s\n",a);
  return 0;
  }
