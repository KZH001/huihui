#include <stdio.h>
#include <string.h>
int main ()
{
  char a[20];
  char b[20]="hello";
  strcpy(a,b);
  printf("%s\n",a);
  return 0;
}

#include <stdio.h>
char mystrcpy(char *i,char *j)
// {
//   while((*i++ = *j++))
//   *i='\0';
// }
{
char *p=i;
while(*j!='\0')
{
*p=*j;*p++;*j++;
}
*p='\0';
return *i;
}
int main ()
{
  char a[20]="world";
  char b[20]="hello";
  mystrcpy(a,b);
  printf("%s\n",a);
  return 0;
}
