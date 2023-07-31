#include <stdio.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */

int _strcmp(char *s1, char *s2);

int main(void)
{
    char s1[] = "Hello";
    char s2[] = "World!";

    printf("%d\n", _strcmp(s1, s2));
    printf("%d\n", _strcmp(s2, s1));
    printf("%d\n", _strcmp(s1, s1));
    return (0);
}

int _strcmp(char *s1, char *s2)
{
    int i;
    int p;
    
    i = 0;
    while (s1[i] != '\0' || s2[i] != '\0')
    {
        if (s1[i] == s2[i])
            p = 0;
        else
        {
            p = s1[i] - s2[i];
            break;
        }
        i++;
    }
    return (p);
}