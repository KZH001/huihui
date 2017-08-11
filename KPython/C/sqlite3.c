#include <stdio.h>
#include <sqlite3.h>
#include <stdlib.h>
#include <string.h>

int call_back(void * a,int columm,char **value,char **name);
void do_select(sqlite3 *);
void do_insert(sqlite3*);

int main(int argc, char const *argv[]) {
  sqlite3 *db = NULL;
  int num = 0;

  if (sqlite3_open("./test.db", &db) != SQLITE_OK)
	{
		printf("%s\n", sqlite3_errmsg(db));
		exit(1);
	}

loop:
  printf("******************************\n");
  printf("****1 select   2 insert*******\n");
  printf("******************************\n");
  scanf("%d",&num);
  switch(num){
    case 1:
    do_select(db);
    break;
    case 2:
    do_insert(db);
    break;
    default:
      goto loop;
  }

  sqlite3_close(db);

  return 0;
}
int call_back(void *a, int column, char **value, char **name)
{
  int i = 0;
	int ret = (*(int*)a)++;
  if ( ret == 0)
  {		//输出该表格的列名, column 是列的个数
    for (i = 0; i < column; i++)
    {
      printf("%-10s", *(name)++);
    		}
    		putchar(10);
    	}	//输出符合条件的一条数据
    	for (i = 0; i < column; i++)
    	{
    		printf("%-10s", *(value)++);
    	}
    	printf("\n");
    	return 0;
    }
    void do_select(sqlite3 *db)
    {
      char *errmsg;
      int a = 0;
      if (sqlite3_exec(db, "select * from stu", call_back, &a, &errmsg ) != SQLITE_OK)
    	{
    		printf("%s\n", errmsg);
    		sqlite3_close(db);
    		return;
    	}
    	sqlite3_close(db);
    	return;
    }
    void do_insert(sqlite3*db)
    {
      char *errmsg;
      int id;
      char name[20] = {0};
      char sql[128] = {0};
      printf("input id(int) >>");
      scanf("%d",&id);
      printf("input name(string) >>");
      scanf("%s",name);
      sprintf(sql,"insert into stu values(%d,'%s')",id,name);
      if (sqlite3_exec(db, sql, NULL, NULL, &errmsg ) != SQLITE_OK)
    	{
    		printf("%s\n", errmsg);
    		return;
    	}
      return;
    }
