#include <stdio.h>
#include <string.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */

char *_strncat(char *dest, char *src, int n);

int main(void)
{
    char s1[98] = "Hello ";
    char s2[] = "World!\n";
    char *ptr;

    printf("%s\n", s1);
    printf("%s", s2);
    ptr = _strncat(s1, s2, 1);
    printf("%s\n", s1);
    printf("%s", s2);
    printf("%s\n", ptr);
    ptr = _strncat(s1, s2, 1024);
    printf("%s", s1);
    printf("%s", s2);
    printf("%s", ptr);
    return (0);
}

char *_strncat(char *dest, char *src, int n)
{
    int i;
    int len1;
    
    len1 = strlen(dest);
    for (i = 0; i < n; i++)
    {
        if (src[i] != '\0')
            dest [i + len1] = src[i];
        else
            break;
    }
    return (dest);
}