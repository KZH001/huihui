#include <stdio.h>
#include <sqlite3.h>//使用sqlite3的接口时,必须要添加
#include <stdlib.h>

int  call_back(void * a, int column, char ** value, char **name);
void do_select(sqlite3 *db);
void do_select_1(sqlite3 *db);
void do_insert(sqlite3 *db);
void do_delete(sqlite3 *db);
void do_update(sqlite3 *db);

int main(int argc, const char *argv[])
{
	sqlite3 *db;
	int cmd;
	char clean[128] = {0};

	if (sqlite3_open("./test.db", &db) != SQLITE_OK)
	{
		printf("%s\n", sqlite3_errmsg(db));//输出错误
		exit(1);
	}

	while (1)
	{
		puts("-----------------command -------------------------------");
		puts("--1: insert  2: delete  3: update  4: select 5:quit-------");
		puts("---------------------------------------------------------");
		printf("input command >>");

		if (scanf("%d", &cmd) != 1)
		{
			puts("input error !");
			fgets(clean, 128, stdin);//清空缓冲区
			continue;
		}

		switch (cmd)
		{
		case 1:
			do_insert(db);
			break;
		case 2:
			do_delete(db);
			break;
		case 3:
			do_update(db);
			break;
		case 4:
			do_select(db);
			break;
		case 5:
			goto EXIT;
		default:
			break;
		}
	}

EXIT:
	sqlite3_close(db);//不要进行多重关闭
	return 0;
}

//只有在查询的时候用到
int call_back(void * a, int column, char ** value, char **name)
{
	int i;
	int ret = (*((int*)a))++;

	//只让字段输出一次
	if (ret == 0)
	{
		for (i = 0; i < column; i++)
		{
			printf("%-10s", *(name++));
		}
		putchar(10);
	}

	for (i = 0; i < column; i++)
	{
		printf("%-10s", *(value++));
	}
	putchar(10);

	return 0;
}

void do_select(sqlite3 *db)
{
	char *errmsg;
	int a = 0;
	if (sqlite3_exec(db, "select * from stu", call_back, &a, &errmsg ) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		return;
	}

	return;
}

void do_select_1(sqlite3 *db)
{
	int nrow, ncolumn;
	char *errmsg;
	char **result, **temp;
	int i, j;

	if (sqlite3_get_table(db, "select * from stu", &result, &nrow, &ncolumn, &errmsg) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		return;
	}

	temp = result;

	//nrow只是符合条件的记录数,字段名不包括在内
	//但是result中包含字段名,如果需要输出包括字段名在内
	//的所有信息,则必须将nrow + 1
	for (i = 0; i < nrow + 1;  i++)
	{
		for (j = 0; j < ncolumn; j++)
		{
			printf("%-10s", *(result++));
		}
		putchar(10);
	}

	sqlite3_free_table(temp);
	return;
}

void do_insert(sqlite3 *db)
{
	char *errmsg;
	int id, age, score;
	char name[20] = {0};

	char sql[128] = {0};

	printf("input id(int) >>");
	scanf("%d", &id);

	printf("input name(string) >>");
	scanf("%s", name);

	printf("input age(int) >>");
	scanf("%d", &age);

	printf("input score(int) >>");
	scanf("%d", &score);

	sprintf(sql, "insert into stu values(%d, '%s', %d, %d)", id, name, age, score);


	if (sqlite3_exec(db, sql ,NULL ,NULL, &errmsg ) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		return;
	}
	puts("insert OK!");

	return;
}

void do_delete(sqlite3 *db)
{
	char *errmsg;
	int id;
	char sql[128] = {0};

	printf("input id(int) >>");
	scanf("%d", &id);

	sprintf(sql, "delete from stu where id = %d", id);

	if (sqlite3_exec(db, sql ,NULL ,NULL, &errmsg ) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		return;
	}
	puts("delete OK!");

	return;
}

void do_update(sqlite3 *db)
{
	char *errmsg;
	int id, score;
	char sql[128] = {0};

	printf("input id(int) >>");
	scanf("%d", &id);

	printf("input update score (int) >>");
	scanf("%d", &score);

	sprintf(sql, "update stu set score = %d  where id = %d", score, id);

	if (sqlite3_exec(db, sql ,NULL ,NULL, &errmsg ) != SQLITE_OK)
	{
		printf("%s\n", errmsg);
		return;
	}
	puts("update OK!");

	return;
}
