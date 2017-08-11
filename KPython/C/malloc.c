// #include <stdio.h>
// #include <stdlib.h>
// typedef int datatype;
// typedef struct node
// {
//   datatype data;
//   struct node *next;
// }linknode,*linklist;
// int main(int argc, char const *argv[]) {
//   linklist p=NULL;
//   if((p=malloc(sizeof(linknode)))==NULL)
//   {
//     printf("malloc error!");
//     return 0;
//   }
//   p->next=NULL;
//   return 0;
// }

#include <stdio.h>
#include <stdlib.h>
typedef int datatype;
typedef struct node
{
  datatype data;
  struct node *next;
}linknode,*linklist;
/*函数封装*/  /*创建链表*/
linklist link_create()
{
  linklist p=NULL;
  if((p=malloc(sizeof(linknode))) == NULL)
  {
    printf("malloc error !\n");
    return NULL;
  }
  p->data=0;
  p->next=NULL;
  return p;
}//*函数2*/
void link_show(linklist H)
{
  while(H!=NULL)
  {
    printf("%d",H->data);
    H=H->next;
  }
  printf("\n");
}

/*创建堆 节点空间*/  /*释放空间*/
// int main(int argc, char const *argv[]) {
//   linklist p=NULL;
//   if((p=malloc(sizeof(linknode)))==NULL)
//   {
//     printf("malloc error!");
//     return 0;
//   }
//   p->next=NULL;
//
//   return 0;
// }
int main(int argc, char const *argv[]) {
  linklist H=NULL;
  if((H=link_create())==NULL)
  {
    printf("create link failed\n");
    return -1;
  }
link_show(H);
  return 0;
}
