#include <stdio.h>

int main() {
    int num = 123456;
    int count = 0;
    while (num != 0) {
        num /= 10;
        ++count;
    }
    printf("The number of digits in %d is: %d\n", num, count);
    return 0;
}