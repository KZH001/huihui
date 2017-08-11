#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sqlite3.h>

int main()
{
	//定义数据库句柄
	sqlite3 *db;
	char *errmsg;

	//出错判断
	if (sqlite3_open("./my.db", &db) != SQLITE_OK)
	{
		//打印出错原因
		printf("%s\n", sqlite3_errmsg(db));
		return -1;
	}


	char sql[256];
	strcpy(sql, "create table stu (id integer not null primary key, name text not null, age integer not null)");

	//不用的参数，填写为NULL
	//执行sql语句
	int ret;
	if ((ret = sqlite3_exec(db, sql, NULL, NULL, &errmsg)) != SQLITE_OK)
	{
		//不是已经存在的错误，那么必须退出
		if (ret != 1)
		{
			//打印出错原因
			printf("%s\n", errmsg);
			sqlite3_close(db);
			return -1;
		}
	}

	printf("table stu already exists, but continue ....\n");


	//关闭数据库
	sqlite3_close(db);
	return 0;
}
