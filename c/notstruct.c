#include <stdio.h>

struct student
{
    char name[20];
    int age;
    float height;
};

int main(void)
{
    int i;

    struct student s[3] = {
        {"techWhiz", 18, 5.0},
        {"codeboy", 15, 4.3},
        {"tech", 17, 4.8}
    };
    printf("%d\n", (sizeof(s)/28));

    for (i = 0; i < 3; i++)
    {
        printf("Name: %s\n", s[i].name);
        printf("Age: %d\n", s[i].age);
        printf("Height: %.1f\n", s[i].height);
        putchar('\n');
    }
    return (0);
}