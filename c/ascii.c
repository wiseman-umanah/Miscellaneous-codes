#include <stdio.h>

char *_memset(char *s, char b, unsigned int n);
int main()
{
    char b[98];
    unsigned int bn = 95;
    char a = 'a';

    *_memset(b, a, bn);

    // for (int i = 0; i < 98; i++)
    // {
    //     printf("%c", b[i]);
    // }
    putchar('\n');

    *_memset(b, a, bn);
    return (0);
}

char *_memset(char *s, char b, unsigned int n)
{
    int i;

    for (i = 0; i < n+1; i++)
    {
        s[i] = b;
        printf("%c", s[i]);
    }
    return (0);
}