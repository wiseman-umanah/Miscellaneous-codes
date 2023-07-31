#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * main - check the code for ALX School students.
 *
 * Return: Always 0.
 */

char *argstostr(int ac, char **av);

int main(int ac, char *av[])
{
    char *s;

    s = argstostr(ac, av);
    if (s == NULL)
    {
        return (1);
    }
    printf("%s", s);
    free(s);
    return (0);
}

char *argstostr(int ac, char **av)
{
    int i, j, len = 0;
    char *str;

    if (ac == 0 || av == NULL)
        return (NULL);

    /* calculate the total length of the arguments */
    for (i = 0; i < ac; i++)
        for (j = 0; av[i][j]; j++)
            len++;

    /* allocate memory for the concatenated string */
    str = malloc(sizeof(char) * (len + ac + 1));
    if (str == NULL)
        return (NULL);

    /* concatenate the arguments */
    for (i = 0, len = 0; i < ac; i++)
    {
        for (j = 0; av[i][j]; j++)
            str[len++] = av[i][j];
        str[len++] = '\n';
    }
    str[len] = '\0';

    return (str);
}
