#include <stdio.h>
#include <stddef.h>
#include <stdarg.h>
#include <string.h>

void print_all(const char * const format, ...)
{
    int i, len, j;
    char * str = "cifs";
i = 0;
len = 0; 

while (format[i] != '\0') {
    j = 0;
    while (str[j] != '\0') {
        if (str[j] == format[i]) {
            ++len;
            break;
        }
        ++j;
    }
    ++i;
}
}
/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    print_all("cecs", 'B', 3, "stSchool");
    return (0);
}