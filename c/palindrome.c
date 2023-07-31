// #include <stdio.h>
// #include <string.h>
#include <stdio.h>
#include <string.h>
 int is_palindrome(char *s);
// void forwardstr(char *str, char *s);
// void backwardstr(char *btr, char *s);

int main(void)
{
     int r;

    r = is_palindrome("level");
     printf("%d\n", r);
     r = is_palindrome("redder");
    printf("%d\n", r);
    r = is_palindrome("test");
    printf("%d\n", r);
     r = is_palindrome("step on no pets");
     printf("%d\n", r);
     return (0);
}

// int is_palindrome(char *s)
// {
//     char str[strlen(s) + 1];
//     char btr[strlen(s) + 1];

//     forwardstr(str, s);
//     backwardstr(btr, s);

//     str[strlen(s)] = '\0';
//     btr[strlen(s)] = '\0';

//     return strcmp(str, btr) == 0;
// }

// void forwardstr(char *str, char *s)
// {
//     if (*s == '\0') {
//         *str = '\0';
//     } else {
//         *str = *s;
//         forwardstr(str + 1, s + 1);
//     }
// }

// void backwardstr(char *btr, char *s)
// {
//     if (*s == '\0') {
//         *btr = '\0';
//     } else {
//         backwardstr(btr, s + 1);
//         *btr = *s;
//         btr++;
//     }
// }





int is_palindromefor(char *s, int start, int end);

/**
 * is_palindrome - checks if a string is a palindrome
 * @s: the string to check
 * @start: the starting index of the string
 * @end: the ending index of the string
 *
 * Return: 1 if the string is a palindrome, 0 otherwise
 */
int is_palindromefor(char *s, int start, int end)
{
    if (start >= end)
        return (1);
    if (s[start] != s[end])
        return (0);
    return (is_palindromefor(s, start + 1, end - 1));
}

/**
 * is_palindrome - checks if a string is a palindrome
 * @s: the string to check
 *
 * Return: 1 if the string is a palindrome, 0 otherwise
 */
int is_palindrome(char *s)
{
    int len = strlen(s);

    return (is_palindromefor(s, 0, len - 1));
}