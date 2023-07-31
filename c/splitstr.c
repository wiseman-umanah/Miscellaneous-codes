#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_tab - Prints an array of string
 * @tab: The array to print
 *
 * Return: nothing
 */
void print_tab(char **tab)
{
    int i;

    for (i = 0; tab[i] != NULL; ++i)
    {
        printf("%s\n", tab[i]);
    }
}

char **strtow(char *str)
{
    char **string;
    if (str == NULL)
    {
        return (NULL);
    }
    
    else
    {
        int i;
        string = (char **)malloc(sizeof(char *) * strlen(str) + 1);
        printf("%ld\n", strlen(str));
        if (string == NULL)
        {
            return (NULL);
        }
        else
        *string = "hello\nworld";
            printf("%p\n", string);
            printf("%s", *string);
        //{
        //     for (i = 0; i < strlen(str); i++)
        //     {
        //         if (*str[i] != '\0')
        //         {
        //             string[i] = str[i];
        //         }
        //     }
        //     return (string);
        // }
        free(string);
    }
}

/**
 * main - check the code for ALX School students.
 *
 * Return: 1 if an error occurred, 0 otherwise
 */
int main(void)
{
    char **tab;

    tab = strtow("      ALX School         #cisfun      fiweifi    iweifuweiw");
    if (tab == NULL)
    {
        printf("Failed\n");
        return (1);
    }
    print_tab(tab);
    return (0);
}