#include<stdio.h>
#include<stdlib.h>
#include<string.h>

unsigned int m=2;
unsigned int cnt=1;

void Factor(int n, char *msg, char printYes);
int main()
{
    char s[100]={0};
    char flag='y';
    printf("------求整数的因式分解------\n请输入正整数m(>1):");
    scanf("%u", &m);
    printf("打印详细分解情况吗？[y|n，回车打印]");
    scanf("%*c%c",&flag);
    if(m<1)
    {
        printf("error input!\n");
        exit(-1);
    }
    if(flag!='n')
        printf("%d =  %d \n", m,m);
    Factor(m, s,flag);
    if(cnt==1)
        printf("\n%d是素数\n",m);
    printf("\n------");
    printf("一共有%d种", cnt);
    printf("------\n");
    return 0;
}

void Factor(int n, char *msg,char printYes)
{
    char s2[100]={0};//保存当前分解的部分结果
    if(n==1)
        return ;
    for(int i=2;i<n;i++)
    {
        if (n%i==0)
        {
            if(n==m)
                sprintf(msg, "%d = ", m);
            sprintf(s2,"%s %d * ",msg, i);//因式分解部分结果保存在字符串s2中

            if(printYes!='n')
                printf("%s %d\n",s2,n/i);//打印结果（包括最后一个因子）
            Factor(n/i,s2,printYes);
            cnt++;
        }
    }
}
