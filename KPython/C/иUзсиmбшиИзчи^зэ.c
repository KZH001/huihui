#include <stdio.h>
void cr(int a[],int n)
{
  int i,j,k;
  for(i=1;i<n;i++)
  {
    k=a[i];
    j=i-1;
    while(j>=0&&k<a[j])
    {
      a[j+1]=a[j];
      j--;
    }
    a[j+1]=k;
  }
}
int main ()
{
  int a[8]={2,1,3,5,4,6,8,7};
  cr(a,8);
  int i;
  for(i=0;i<8;i++)
  {
    printf("%d",a[i]);
  }
  printf("\n");
  return 0;
}












// int main(int argc, char const *argv[])
// {
//   int a[8]={2,4,6,7,9,1,3,5};
//   cr(a,8);
//   for(int i=0;i<8;i++)
//   {
//     printf("%d",a[i]);
//   }
//   printf("\n");
//   return 0;
// }
