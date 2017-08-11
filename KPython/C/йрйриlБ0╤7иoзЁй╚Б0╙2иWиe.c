#include <stdio.h>
int main ()
{
  //**冒泡排序**//
  int a[6]={3,6,8,2,7,9};
  int i,j,k;
  for(i=0;i<6-1;i++)
  {
    for(j=0;j<6-i-1;j++)
    {
      if(a[j]>a[j+1])
      {
        k=a[j];
        a[j]=a[j+1];
        a[j+1]=k;

      }
    }
  }
  for(i=0;i<6;i++)
  printf("%d",a[i]);
  printf("\n");
  return 0;

}
      //**插入排序**//
   int a[6]={3,4,7,2,8,9};
   int i,j,k;
   for(i=0;i<6;i++)
   {
     k=a[i];j=i-1;
     while(j>=0&k<a[j])
     {
    a[j+1]=a[j];j--;
     }

   a[j+1]=k;
 }
 for(i=0;i<6;i++)
 printf("%d",a[i]);
 printf("\n");
 return 0;
 }

//**选择排序**//
int a[6]={3,5,7,2,1,6};
int i,j,k,x;
for(i=0;i<6;i++)
{
  k=i;
  for(j=i+1;j<6-1;j++)
  {
    if(a[k]>a[j])
    {
      k=j;
    }
  }
  if(i!=k)
  {
    x=a[i];
    a[i]=a[k];
    a[k]=x;
  }
}
for(i=0;i<6;i++)
printf("%d",a[i]);
printf("\n");
return 0;
}

//**数组最大值**//
int a[5]={4,3,6,7,8};
int i,j;
for(i=1;i<5;i++)
{
  if(a[j]<a[i])
  {
    j=i;
  }
}
printf("a[%d]=%d",j,a[j]);
return 0;
}
