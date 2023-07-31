#include <stdio.h>
#include <stdarg.h>

/**
* sum_them_all - finds the sum of n numbers
*
* @n: number of args
* Return: return sum if success, 0 otherwise
*/

int sum_them_all(const unsigned int n, ...)
{
        unsigned int i, result, x;
        va_list args;

        if (n <= 0)
                return (0);

        va_start(args, n);
        result = 0;
        for (i = 0; i < n; i++)
        {
                x = va_arg(args, unsigned int);
                result += x;
        }
        va_end(args);
        return (result);
}

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    int sum;

    sum = sum_them_all(2, 98, 1024);
    printf("%d\n", sum);
    sum = sum_them_all(4, 98, 1024, 402, -1024);
    printf("%d\n", sum);    
    return (0);
}