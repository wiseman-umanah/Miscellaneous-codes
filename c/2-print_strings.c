#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>


void print_strings(const char *separator, const unsigned int n, ...)
{
    unsigned int i;
    char *str;
    va_list args;

    va_start(args, n);
    for (i = 0; i < n; i++)
    {
        str = va_arg(args, char *);
        if (str == NULL)
            printf("(nil)");
        else
        {
            printf("%s", str);
        }
        if (i < n-1 && separator != NULL)
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
    print_strings(", ", 2, NULL, "Django");
    return (0);
}