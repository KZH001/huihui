#include <stdio.h>
int main()
{
   int jo(int x,int y);
   int a[10],b[10],c,n=0,m=0,l=0;
   for(c=0;c<10;c++)
   scanf("%d",&a[c]);
   printf("\n");
   printf("b: \n");
   for(c=0;c<10;c++)
   scanf("%d",&b[c]);
   printf("\n");
   for(c=0;c<10;c++)
    {
      if(jo(a[c],b[c])==1)n=n+1;
      else if(jo(a[c],b[c])==0)m=m+1;
      else l=l+1;
    }
  printf("a[c]>b[c]%d times\n a[i]=b[i]%d times\n a[c]<b[c]%d times\n",n,m,l);
  if(n>l)  printf("array a is larger than array b\n");
  else if(n<l) printf(" array a is smallerr than arrayb\n");
  else  printf("array a is equal than array b\n");
}
   int jo(int x,int y)
    {
      int flag;
      if(x>y)flag=1;
      else if(x<y)flag=-1;
      else flag=0;
     return flag;
   }



#include <stdio.h>
int kk(int *a,int b)
{
  int i,j,k;
  for(i=0;i<10;i++)
  {
    for(j=0;j<10;j++)
    {
      if(a[i]%2!=0&&a[j]%2==0)
      {
        k=a[i];a[i]=a[j];a[j]=k;
      }
    }
  }
}
int main ()
{
  int a[10]={5,4};
  int i;
  kk(a,10);
  for(i=0;i<10;i++)
    {
      printf("%d",a[i]);
    }
  printf("\n");
  return 0;
}
