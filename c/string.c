#include <stdio.h>
#include <string.h>

int main()
{
    char s[11] = "Holberton!";
    int i;
    char p[strlen(s)]; 
    for (i = (strlen(s) - 1); i >= 0; i--)
    {
        for (int j = 0; j < strlen(s); j++)
        {
            p[j] = s[j];
        }
    }
    puts(p);
}