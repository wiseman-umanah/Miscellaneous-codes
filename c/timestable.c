#include <stdio.h>

int main()
{
    int ok;
    int user;
    int j;
    int k;

    printf("Please use fullscreen view for a better view");
    printf("\nPlease enter a number(1-30): ");
    scanf("%d", &user);
    printf("\n");

    if (user <= 0 || user > 30)
    {
        printf("Number is too high or low\nOr your input is not a number\n");
    }
    else
    {
        for (j = 1; j <= 20; j++)
        {
            for (k = 1; k <= user; k++)
            {
                printf("%5d", j * k);
            }
        printf("\n");
        }
        printf("\n");
    }
    printf("Thank you for using this program\nAuthor: Wiseman Umanah\nContact me: wisemanumanah@gmail.com\n");
    scanf("%d", &ok);
    printf("%d",ok);
    return 0;
}