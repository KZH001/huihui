// <!DOCTYPE html>
// <html lang="en">
// <head>
//   <meta charset="UTF-8">
//   <meta name="viewport" content="width=device-width, initial-scale=1.0">
//   <meta http-equiv="X-UA-Compatible" content="ie=edge">
//   <title>Document</title>
// </head>
// <body>
//
//   <form action="cgi-bin/cgi" method="GET">
//       a = : <input type="text" name="a" />
//       +
//       b = : <input type="text" name="b" />
//       <input type="submit" name="" value="Sumbit">
//   </form>
// </body>
// </html>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
  char a[100];
  long i, j;
  char *data;
  printf("Content type: text/html\n\n");
  printf("<html lang=\"en\">\n");
  printf("<meta charset=\"UTF-8\">\n");
  printf("<head><title>An html page from a cgi</title>\n");
  printf("<style type=\"text/css\">");
  printf("</style></head>");
  printf("<body>\n");
  data = getenv("QUERY_STRING");
  if(data == NULL)
    printf("error!!!\n");
  printf("%s\n", data);
  sscanf(data, "a=%ld&b=%ld", &i, &j);
  printf("fname=%ld\n", i + j);
  printf("</body>\n");
  printf("</html>\n");

  fflush(stdout);
  return 0;
}
