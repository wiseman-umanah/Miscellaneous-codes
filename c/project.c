#include <limits.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <stdarg.h>

/**
 * main - Entry point
 *
 * Return: Always 0
 */

int _printf(const char *format, ...);
int _putchar(char c);

int main(void)
{
    int len;
    int len2;
    unsigned int ui;
    void *addr;

    // len = _printf("Let's try to printf a simple sentence.\n");
    // len2 = printf("Let's try to printf a simple sentence.\n");
    // ui = (unsigned int)INT_MAX + 1024;
    // addr = (void *)0x7ffe637541f0;
    // _printf("Length:[%d, %i]\n", len, len);
    printf("Length:[%d, %i]\n", len2, len2);
    // _printf("Negative:[%d]\n", -762534);
    // printf("Negative:[%d]\n", -762534);
    // _printf("Unsigned:[%u]\n", ui);
    // printf("Unsigned:[%u]\n", ui);
    // _printf("Unsigned octal:[%o]\n", ui);
    // printf("Unsigned octal:[%o]\n", ui);
    // _printf("Unsigned hexadecimal:[%x, %X]\n", ui, ui);
    // printf("Unsigned hexadecimal:[%x, %X]\n", ui, ui);
    _printf("Character:[%c]\n", 'H');
    printf("Character:[%c]\n", 'H');
    // _printf("String:[%s]\n", "I am a string !");
    // printf("String:[%s]\n", "I am a string !");
    // _printf("Address:[%p]\n", addr);
    // printf("Address:[%p]\n", addr);
     len = _printf("Percent:[%%]\n");
     len2 = printf("Percent:[%%]\n");
    // _printf("Len:[%d]\n", len);
    // printf("Len:[%d]\n", len2);
    // _printf("Unknown:[%r]\n");
    // printf("Unknown:[%r]\n");
    return (0);
}

int _putchar(char c)
{
    return (write(1, &c, 1));
}

int _printf(const char *format, ...)
{
    va_list args; /*list of args*/
    int count = 0;

    va_start(args, format);

    while (*format != '\0')
    {
        if (*format == '%')
        {
            format++;
            if (*format == 'c')
            {
                char c = va_arg(args, int);
                _putchar(c);
                count++;
            }
            else if (*format == 's')
            {
                char *s = va_arg(args, char *);
                while (*s != '\0')
                {
                    _putchar(*s);
                    s++;
                    count++;
                }
            }
            else if (*format == '%')
            {
                _putchar('%');
                count++;
            }
            else if (*format == 'd')
            {
                char *d = (char *)malloc(sizeof(int));
                d = (char *)va_arg(args, int);
                while (*d != '\0')
                {
                    _putchar(*d);
                    d++;
                    count++;
                }
            }
        }
        else
        {
            _putchar(*format);
            count++;
        }
        format++;
    }

    va_end(args);

    return count;
}