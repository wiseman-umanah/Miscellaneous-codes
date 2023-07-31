#include <stdio.h>
#include <stdlib.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */

char *string_nconcat(char *s1, char *s2, unsigned int n)
{
    unsigned int i;
    int tlen;
    int tlen2;
    char *ptr;

    i = tlen = 0;
    if (s1 == NULL)
    {
        s1 = " ";
    }
    if (s2 == NULL)
    {
        s2 = " ";
    }
    while (s1[i] != '\0')
    {
        tlen ++;
        i++;
    }
    tlen2 = tlen + n + 1;
    ptr = malloc(tlen2 * sizeof(char));

    if (ptr ==NULL)
        return (NULL);
    i = 0;
    while (s1[i] != '\0')
    {
        ptr[i] = s1[i];
        i++;
    }
    i = 0;
    while (s2[i] != '\0')
    {
        while (i < n)
        {
            ptr[i + tlen] = s2[i];
            i++;
        }
        i++;
    }
    ptr[tlen2 - 1] = '\0';
    
    return (ptr);
}


int main(void)
{
    char *concat;

    concat = string_nconcat(NULL, "HELLO", 0);
    printf("%s\n", concat);
    free(concat);
    return (0);
}