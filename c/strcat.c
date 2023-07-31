/*#include <stdio.h>
#include <string.h>

char *_strcat(char *dest, char *src);

int main()
{
    char s1[98] = "Hello ";
    char s2[] = "World!\n";
    char *ptr;

    printf("%s\n", s1);
    printf("%s", s2);
    ptr = _strcat(s1, s2);
    printf("%s", s1);
    printf("%s", s2);
    printf("%s", ptr);
    return (0);    
}

char *_strcat(char *dest, char *src)
{
    int i;
    int len1;
    int len2;

    len1 = strlen(dest);
    len2 = strlen(src);

    i = 0;
    for (; i <= len2; i++)
    {
        dest[i + len1] = src[i];
    }
    return (dest);
}
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * main - check the code for ALX School students.
 *
 * Return: Always 0.
 */
char *str_concat(char *s1, char *s2);

int main(void)
{
    char *s;

    s = str_concat(NULL, "hi");
    if (s == NULL)
    {
        printf("failed\n");
        return (1);
    }
    printf("%s\n", s);
    free(s);
    return (0);
}

 /**
  5 * str_concat - string concatenation with malloc
  6 *
  7 * @s1: first string
  8 * @s2: second string
  9 *
 10 * Return: returns pointer to string or NULL if false
 11 */
 
 char *str_concat(char *s1, char *s2)
 {
          char *ptr;
          int len1;
         int len2;
          int tlen;
 
          if (s1 == NULL)
            s1 = "";
          if (s2 == NULL)
             s2 = "";
         len2 = strlen(s2);
          len1 = strlen(s1);
          tlen = len1 + len2 + 1;
          ptr = (char *)malloc(tlen);
         if (ptr == NULL)
          {
                  return (NULL);
          }
          strcpy(ptr, s1);
          strcat(ptr, s2);
          ptr[tlen] = '\0';
          return (ptr);
 }