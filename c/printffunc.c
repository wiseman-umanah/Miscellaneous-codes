#include <unistd.h>
#include <stdarg.h>


/**
 * _putchar - writes the character c to stdout
 * @c: The character to print
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
int _putchar(char c)
{
    return (write(1, &c, 1));
}

/*
change int to str*/
char *int_to_str(int num, char *str) {
    int i = 0;
    int is_negative = 0;
    if (num < 0) {
        is_negative = 1;
        num = -num;
    }
    if (num == 0) {
        str[i++] = '0';
    }
    while (num > 0) {
        str[i++] = num % 10 + '0';
        num /= 10;
    }
    if (is_negative) {
        str[i++] = '-';
    }
    str[i] = '\0';
    int len = i;
    for (i = 0; i < len / 2; i++) {
        char tmp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = tmp;
    }
    return str;
}


/*
This is the printf function.
*/
void _printf(char *str, ...)
{
    va_list args;

    if (args == NULL)
    {
        for (int i = 0; str[i] != '\0'; i++)
        {
            _putchar(str[i]);
        }
    }
    else
    {
        va_start(args, str);
        int i = 0;
        while (str[i] != '\0')
        {
            /**if (str[i] == '%' && str[++i] == 'c')
            {
                if (str[++i] == 'c')
                    continue;
                _putchar(va_arg(args, int));
            }*/
            if (str[i] == '%' && str[++i] == 'd')
            {
                if (str[++i] == 'd')
                    continue;
                int x = va_arg(args, int);
                 char strgy[3];
                char *result = int_to_str(x, strgy);
                for (i = 0; result[i] != '\0'; i++)
                {
                    _putchar(result[i]);
                }
            }
            _putchar(str[i]);
            i++;
        }
        va_end(str);
    }
}
int main()
{
    int pi = 98;
    _printf("Hello, world %d", pi);
    return (0);
}
