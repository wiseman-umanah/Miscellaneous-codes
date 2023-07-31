#include <stdio.h>

struct student
{
    char name[20];
    int age;
    float height;
};

int main(void)
{
    struct student s = {"techWhiz", 18, 5.0};

    struct student *ptr;
    ptr = &s;

    printf("%s\n", ptr->name);
    printf("%d\n", (*ptr).age);
    printf("%.1f\n", (*ptr).height);
    
    return (0);
}