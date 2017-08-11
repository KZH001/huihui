#include <stdio.h>
typedef struct Student
{
  int id;
  char name[64];
  int age;
  float salary;
}Stu;
// typedef struct Student Stu;
int main ()
{
  Stu a;
  a.id=1;
  printf("%d\n",1);
  return 0;
}
