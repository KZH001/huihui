/*链表*/
#include <stdio.h>
 // /*typedef 重命名*/
 // /*第一个结构体*/
 // typedef struct stu
 // {
 //   int id;
 //   char name[65];
 //   int age;
 // };
 typedef int datatype;
 /*第二个结构体*/
 // struct node
 // {
 //   datatype data; /*数据*/
 //   struct node *next; /*指针*/
 // };
 typedef struct node
 {
   datatype data;
   struct node *next;
 }linknode,*linkkang;
 int main(int argc, char const *argv[]) {
  //  struct node a={{1,"kang",24},NULL};
  // struct node a={1,NULL};
  linknode a={1,NULL};
 // struct node *head=&a;
 linkkang head =&a;
  //  printf("5s\n",head->data.name);
  printf("%d\n",head->data);
   return 0;
 }
