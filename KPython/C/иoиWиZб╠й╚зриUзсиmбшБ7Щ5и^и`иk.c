#include <stdio.h>
#include <string.h>
int main ()
{
  char a[20]="hello";
  char b[20]="world";
  int c;
  c=strcmp(a,b);
  printf("%d\n",c);
  return 0;
}


#include <stdio.h>
 int mystrcmp(char *a,char *b)
 {
   while (*a!='\0'&&*b!='\0')
   {
     if(*a>*b)
     return 1;
     if (*a<*b)
     return -1;
   }
   if(*a=='\0'&&*b=='\0')
   return 0;
   if(*a!='\0'&& *b=='\0')
   return 1;
   if(*a=='\0'&&*b!='\0')
   return -1;
 }
 int main ()
 {
   char i[20]="hello";
   char j[20]="world";
   int k;
   k=mystrcmp(i,j);
   printf ("%d\n",k);
   return 0;
 }
