#include <stdio.h>
#include <math.h>
int main ()
{

  float a,b,c,d;
  d=b*b-4*a*c;
  printf("x1=%f",(-b+sqrt(d))/(2*a));
  printf("x2=%f\n",(-b-sqrt(d))/(2*a));
  return 0;
}
float a=2.0,b=3.0,c=1.0;
float x,y;
float x1,x2;
x=-b/(2.0*a);
y=sqrt(b*b-4*a*c)/(2*a);
x1=x+y;
x2=x-y;
printf("x1=%.2f,x2=%.2f\n",x1,x2);
return 0;
}
void A1 (double a,double b,double c,double d);
void A2 (double a,double b,double c,double d);
void A3 (double a,double b,double c,double d);


int main ()
{
  double a,b,c,d;
  scanf("%lf%lf%lf",&a,&b,&c);
  d=b*b-4*a*c;
  if(d>0)
  A1 (a,b,c,d);
  if (d==0)
  A2 (a,b,c,d);
  if (d<0)
  A3 (a,b,c,d);
  return 0;

}
