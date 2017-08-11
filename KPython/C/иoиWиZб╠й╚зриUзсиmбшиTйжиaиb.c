#include <stdio.h>
#include <string.h>
int main ()
{
  char a[20]="hello";
  int i;
  i=strlen (a);
  printf("%d\n",i);
  return 0;
}


#include <stdio.h>
size_t mystrlen(char *a)
{
  int b;
  while (*a++)
  b++;
  return b;
}
int main ()
{
  int i;
  char j[20]="hello";
  i=mystrlen(j);
  printf("%d\n",i);
  return 0;
}
