#include <stdio.h>
#include <stdlib.h>
/**
 * main - check the code for ALX School students.
 *
 * Return: Always 0.
 */

char *_strdup(char *str)
{
    char *spt; 
    if (str == NULL)
    {
        return (NULL);
    }
    else
    {
        spt = malloc(strlen(str)* sizeof(char) + 1);
        if (spt == NULL)
        {
            return (NULL);
        }
        strcpy(spt, str);
        return(spt);
    }
}


int main(void)
{
    char *s;

    s = _strdup("ALX SE");
    if (s == NULL)
    {
        printf("failed to allocate memory\n");
        return (1);
    }
    printf("%s\n", s);
    free(s);
    return (0);
}

