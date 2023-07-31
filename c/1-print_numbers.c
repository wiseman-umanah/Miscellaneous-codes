#include <stdio.h>
#include <stddef.h>
#include <stdarg.h>

void print_numbers(const char *separator, const unsigned int n, ...)
{
        unsigned int i, x;
        va_list args;

        va_start(args, n);
        for (i = 0; i < n; i++)
        {
            x = va_arg(args, int);
            printf("%d", x);
		    if (i < n - 1 && separator != NULL)
			    printf("%s", separator);
        }
        va_end(args);
        printf("\n");
}
/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    print_numbers(", ", 4, 0, 98, -1024, 402);
    return (0);
}