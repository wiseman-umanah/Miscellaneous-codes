#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FORMAT_SPECIFIERS 10

void extract_format_specifiers(char *string, char **format_specifiers) {
    int num_format_specifiers = 0;
    char *ptr = string;
    while (*ptr) {
        if (*ptr == '%') {
            format_specifiers[num_format_specifiers] = ptr;
            num_format_specifiers++;
            if (num_format_specifiers >= MAX_FORMAT_SPECIFIERS) {
                break;
            }
        }
        ptr++;
    }
    format_specifiers[num_format_specifiers] = NULL;
}

int main() {
    char *string = "hello, %d world %s %f";
    char *format_specifiers[MAX_FORMAT_SPECIFIERS + 1];
    extract_format_specifiers(string, format_specifiers);
    for (int i = 0; format_specifiers[i] != NULL; i++) {
        printf("%s\n", format_specifiers[i]);
    }
    return 0;
}