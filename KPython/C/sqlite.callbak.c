#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>

int call_back(void *param, int column, char **value, char **name);

int main()
{

	sqlite3 *db;
	char *errmsg;
	char sql[128];
	int a = 0;

	if (sqlite3_open("./my.db", &db) != SQLITE_OK)
	{
		printf("%s\n", sqlite3_errmsg(db));
		return -1;
	}

	if (sqlite3_exec(db, "select * from stu", call_back, &a, &errmsg ) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		sqlite3_close(db);
		return -1;
	}

	sqlite3_close(db);
	return 0;
}


//每次查询到符合条件的都会被调用一次
int call_back(void *param, int column, char **value, char **name)
{
	int a;
	int i = 0;
	a = (*(int*)param)++;

	if ( a == 0)
	{
		//输出该表格的列名, column 是列的个数
		for (i = 0; i < column; i++)
		{
			printf("%15s", *(name)++);
		}
		putchar(10);
	}

	//输出符合条件的一条数据
	for (i = 0; i < column; i++)
	{
		printf("%15s", *(value)++);
	}

	printf("\n");
	return 0;
}
