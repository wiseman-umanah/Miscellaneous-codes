#include <stdio.h>
#include <ctype.h>
#include <math.h>

int main()
{
    int a[5];
    int i; 

    for (i = 0; i < ((sizeof(a) / sizeof(int))); i++)
    {
        printf("Please type a number: \n");
        scanf("%d", &a[i]);
    }
    printf("\n");
    printf("{");
    for (i = 0; i < 5; i++)
    {
        if (i == 4){
            printf("%d", a[i]);
        }
        else{
            printf("%d, ", a[i]);
        }
        
    }
    printf("}");
    return (0);
}