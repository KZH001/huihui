#include <stdio.h>
struct Stu
{
  int id;
  char name[80];
  int age;
  float salary;
}c={3,"kang",23,10000.0};
struct
{
  int id;
  char name[80];
  int age;
  float salary;
}f;
struct Stu b,d;
int main ()
{
  struct Stu a={1,"li",23,8000.0},e={5,"zhang",22,8000.0};
  a.salary=9000.0;
  a=c;
  printf("%d\n",a.id);
  printf("%s\n",a.name);
  printf("%d\n",a.age);
  printf("%f\n",a.salary);
  printf("%d\n",e.id);
  printf("%s\n",e.name);
  printf("%d\n",e.age);
  printf("%f\n",e.salary);
  printf("%d\n",c.id);
  printf("%s\n",c.name);
  printf("%d\n",c.age);
  printf("%f\n",c.salary);
  return 0;
}
