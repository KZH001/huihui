#include <stdio.h>
int main(int i,  char *j[])
 {
  char * p=j[1];  /*char * p=NULL;*/
   int k=0;
   if(i<2)
   {//  printf("usage:%s string\n",j[0]);
    printf("%s\n",j[0]);    /*  printf("i");*/
     return 0;
   }//  printf("string:%s\n",j[1]);
  printf("%s\n",j[1]);
   p=j[1];
   while(*p)/* *p!='\0'*/
  {
      k=10 * k + *p-'0';
    p++;
   }
   printf("k=%d\n",k);
   return 0;
 }
