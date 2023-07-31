#include <stdio.h>

int main(void){
	int i;
	int j;
	int k;

	for (i = 0; i <= 9; i++)
	{
		for (k = 9; k > i; k--)
		{
			printf(" ");
		}
		for (j = 0; j <= i; j++)
		{
			printf("#");
		}
		printf("\n");
	}
	return 0;
}