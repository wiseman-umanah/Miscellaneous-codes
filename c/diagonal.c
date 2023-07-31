#include <stdio.h>

int main()
{
    int i;
    int j;
    int k;
    int m;

    for (i = 0; i <= 9; i++)
    {
        for (m = 9; m > i; m--)
		{
			printf(" ");
		}
        printf("/");
        for (k = 0; k <= i; k++)
        {
            printf(" ");
        }
        printf("|");
        for (k = 0; k <= i; k++)
        {
            printf(" ");
        }
        printf("\\");
        printf("\n");
    }
}