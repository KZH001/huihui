#include <stdio.h>
int main(int argc, char const *argv[]) {
// char a,b;
// int c;
// scanf ("%c",&a);
// scanf ("%d",&c);
// // getchar();
// scanf (" %c",&b);
// printf("%c %c %d\n",a,b,c);
int cmd;
while (1)
{
  // scanf("%d",&cmd);
  if (scanf("%d", &cmd) != 1)
  {
    puts("input error !");
    fgets(clean, 128, stdin);//清空缓冲区
    continue;
}
  return 0;
}
