#include <stdio.h>
int main()
{
char a[12]="hello world";

a[0]='H';

//char *p="nihao China";

// printf("*p=%c\n",*(p+1));
//*p='N';
char *p;
p=a;


printf("%s\n",a);
printf("%s\n",p);
return 0;
}
