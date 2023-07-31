#include <stdio.h>

int main() {
    int num = 123;
    char str[10];
    sprintf(str, "%c", num);
    printf("The string is: %s\n", str);
    return 0;
}