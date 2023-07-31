#include <stdio.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */

char *rot13(char *s);

int main(void)
{
    char s[] = "ROT13 (\"rotate by 13 places\", sometimes hyphenated ROT-13) is a simple letter substitution cipher.\n";
    char *p;

    p = rot13(s);
    printf("%s", p);
    printf("------------------------------------\n");
    printf("%s", s);
    printf("------------------------------------\n");
    p = rot13(s);
    printf("%s", p);
    printf("------------------------------------\n");
    printf("%s", s);
    printf("------------------------------------\n");
    p = rot13(s);
    printf("%s", p);
    printf("------------------------------------\n");
    printf("%s", s);
    return (0);
}

char *rot13(char *s)
{
        char *p = s;

        while (*p)
        {
                if ((*p >= 'a' && *p <= 'm') || (*p >= 'A' && *p <= 'M'))
                {
                        *p += 13;
                }
                else ((*p >= 'n' && *p <= 'z') || (*p >= 'N' && *p <= 'Z'))
                {
                        *p -= 13;
                }
                p++;
        }
        return (s);
}