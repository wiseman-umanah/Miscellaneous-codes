#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stddef.h>

/**
* main - Entry point
*
* @argc: argumnets count
* @argv: argument vector
*
* Return: Always 0
*/

int main(int argc, char *argv[])
{
        int i;
        long int a, b;
        size_t j;

        if (argc != 3)
        {
                puts("Error");
                exit(98);
        }
        for (i = 1; i < 3; i++)
        {
                for (j = 0; j < strlen(argv[i]); j++)
                {
                        if (!(isdigit(argv[i][j])))
                        {
                                puts("Error");
                                exit(98);
                        }
                }
        }
        a = strtol(argv[1], NULL, 10);
        b = strtol(argv[2], NULL, 10);
        printf("%ld\n", a * b);
        return (0);
}