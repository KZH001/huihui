// #include <stdio.h>
// #include <assert.h>
// void replace(char *i)
// {
//    assert(i);                       //空格转换
//    int OldLen = 0;                  //原字符串长度
//    int NewLen = 0;                  //新字符串长度
//    int BlackNum = 0;                //空格数量
//    int NewBack = 0;                 //新字符串尾部
//    int OldBack = 0;                 //原字符串尾部
//    while (i[OldLen] != '\0')
//    {
//        if (i[OldLen] == ' ')
//        {  BlackNum++;}
//        OldLen++;
//    }
//    NewLen = OldLen + BlackNum * 2;
//    OldBack = OldLen-1;
//    NewBack = NewLen - 1;
//    while (OldBack!=0)
//    {
//        if (i[OldBack] == ' ')
//        {i[NewBack--] = '0';i[NewBack--] = '2';i[NewBack] = '%';}
//      else
//        {i[NewBack] = i[OldBack];}
//        OldBack--;
//        NewBack--;
//    }
// }
// int main()
// {
//    char p[20] = "hello world !";
//    replace(p);
//    printf("%s\n", p);
//    return 0;
// }


// #include <stdio.h>
// int kk (char *a)
// {
//   int i=0;
//   while (a[i]!='\0')
//   {
//     if(a[i]==' ')
//     {
//       a[i]=='-';
//     }
//     else
//     {
//       i++;
//     }
//   }
//   return 0;
// }
// int main ()
// {
//   char a[20]="hello world !";
//   kk(a);
//   printf("%s\n",a);
//   return 0;
// }


#include <stdio.h>
int kk(char *a)
{
  int i=0;
  while(a[i]!='\0')
  {
    if(a[i]==' ')
    {
      a[i]='-';
    }
    else
    {
      i++;
    }
  }
  return 0;
}
int main ()
{
  char a[20]="hello world !";
  kk(a);
  printf("%s\n",a);
  return 0;
}
