#include <stdio.h>
/*结构体指针*/
 typedef/*重命名*/
typedef struct Student
{
  int id;
  char name[64];
  int age;
  float salary;
}Stu;/*,*s;*/
int main ()
{
  struct Student a={1,"kang",23,8000};
    s p;   /*Stu *p;*/  /*struct Student *p;*/
  p=&a;
  printf("%d\n",(*p).id);
  printf("%s\n",p->name);
  return 0;
}
