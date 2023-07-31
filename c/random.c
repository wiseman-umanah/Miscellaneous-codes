#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
* main - Entry point
*
* Return: Always (0)
*/
int main(void)
{
	int i;
	int j;

	srand(time(NULL));

	for (i = 0; i <= 10; i++)
	{
		for (j = 0; j <= 10; j++)
		{
			printf("%c", rand() % 2345 + 1);
		}
		printf("\n");
	}
	return (0);
}