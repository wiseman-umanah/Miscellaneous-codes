#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned int num = 2147484671 + 1024;
    int re;
    int j = 0;
    int *str = malloc(sizeof(int)); // allocate memory for str
    str[0] = 0; // initialize str to all zeros
    while (num != 0)
    {
        num /= 8;
        re = num % 8;
        str[j] = re + 48;
        j++;
        str = realloc(str, (j + 1) * sizeof(int)); // resize str to fit the converted number
        str[j] = 0; // add null terminator to the end of str
    }
    int i = j - 1; // start from the last element of str
    while (i >= 0)
    {
        putchar(str[i]);
        i--;
    }
    free(str); // free the memory allocated for str
    return 0;
}