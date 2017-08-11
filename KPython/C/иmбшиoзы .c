#include <stdio.h>
int main()
{
int i;
int a[6]={1,2,3,4,5,6};
int *p=a;

for(i=0;i<6;i++)
{
  printf("%d",a[i]);
}
printf("\n+++\n");
for(i=0;i<6;i++)
{
  printf("%d",p[i]);
}
printf("\n+++\n");
for(i=0;i<6;i++)
{
  printf("%d",*(p+i));
}
printf("\n+++\n");
for(i=0;i<6;i++)
{
  printf("%d",*(a+i));
}
printf("\n+++\n");
for(i=0;i<6;i++)
{
  printf("%d",*(&a[3]));
}
printf("\n+++\n");
/*a是常量
// for(i=0;i<6;i++)
// {
//   printf("%d",*p++);
// }
// printf("\n");
*/
return 0;
}
