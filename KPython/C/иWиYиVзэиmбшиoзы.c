#include <stdio.h>  //char

int main(int argc, char const *argv[])
{
  char *a[5]={"hello","hi","nihao","how are you","sawadika"};
  int i;
  for(i=0;i<5;i++)
  {
    printf("%s\n",a[i]);
  }
  // printf("%c\n",a[2][0]);
  return 0;
}

//二级指针//
#include <stdio.h>
int main ()
{
  char *kkk[]={"nihao","hello","how are you"};
  char **kk;
  int k;
  for(k=0;k<3;k++)
  {
    kk=kkk+k;
    printf("%s\n",*kk);
  }
  return 0;
}
