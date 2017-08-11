#include<stdio.h>
int main ()
{
  int year,mon,day;
  int a=0;
  int days=0;
  loop:
  printf("日期:\n");
  scanf("%d.%d.%d",&year,&mon,&day);
  if(year<0||mon<1||mon>12||day<1||day>31)
  {printf("有误\n");goto loop;}
  if((mon==4||mon==6||mon||9||mon==11)&&(day>30))
  {printf("有误\n");goto loop;}
  if((year%400==0)||(year%4==0&&year%100!=0))
  {a=1;}
  if(mon==2&&a==0&&day>28)
  {printf("有误\n");goto loop;}
  else if (mon==2&&day>29)
  {printf("有误\n");goto loop;}
  switch(mon)
  {
    case 12 :days+=30;
    case 11 :days+=31;
    case 10 :days+=30;
    case 9 :days+=31;
    case 8 :days+=31;
    case 7 :days+=30;
    case 6 :days+=31;
    case 5 :days+=30;
    case 4 :days+=31;
    case 3 :days+=days+28+a;
    case 2 :days+=31;
    case 1 :days+=day;
}
printf("输入日期在%d年中%d天\n",year,days);
return 0;
}











#include <stdio.h>

int main()
{
int day,month,year,sum,leap;
printf("输入年月日\n");
scanf("%d,%d,%d",&year,&month,&day);
switch(month)/*先计算某月以前月份的总天数*/
{
case 1:sum=0;break;
case 2:sum=31;break;
case 3:sum=59;break;
case 4:sum=90;break;
case 5:sum=120;break;
case 6:sum=151;break;
case 7:sum=181;break;
case 8:sum=212;break;
case 9:sum=243;break;
case 10:sum=273;break;
case 11:sum=304;break;
case 12:sum=334;break;
printf("有误");break;
}
sum=sum+day;
/*再加上某天的天数*/
if(year%400==0||(year%4==0&&year%100!=0))/*判断是不是闰年*/
leap=1;
else
leap=0;
if(leap==1&&month>2)/*如果是闰年且月份大于 2,总天数应该加一天*/
sum++;
printf("今天是%dth day.",sum);}
