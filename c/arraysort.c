#include <stdio.h>
#include <math.h>

int main()
{
    int user;
    float opp;
    float adj;
    float hyp;

    printf("Welcome to the pythagoras calculator\n\n");
    printf("What do you want to calculate\n1. Opposite\n2. Adjacent\n3. Hypotenuse\n\n\tType 1, 2, or 3\n");
    scanf("%d", &user);

    if (user == 1)
    {
        printf("Enter the adjacent:\n");
        scanf("%f", &adj);
        printf("Enter the hypotenuse:\n");
        scanf("%f", &hyp);

        opp = (hyp * hyp) - (adj * adj);
        printf("\nThe opposite side of the triangle is %.2f\n", sqrt(opp));
    }
    
    else if (user == 2)
    {
        printf("Enter the opposite:\n");
        scanf("%f", &opp);
        printf("Enter the hypotenuse:\n");
        scanf("%f", &hyp);

        adj = (hyp * hyp) - (opp * opp);
        printf("\nThe adjacent side of the triangle is %.2f\n", sqrt(adj));
    }

    else if (user == 3)
    {
        printf("Enter the opposite:\n");
        scanf("%f", &opp);
        printf("Enter the adjacent:\n");
        scanf("%f", &adj);

        hyp = (opp * opp) + (adj * adj);
        printf("\nThe hypotenuse of the triangle is %.2f\n", sqrt(hyp));
    }
    else 
    {
        printf("Wrong Input");
    }

    printf("\n\nThank you for using this program\nAuthor: Wiseman Umanah\nContact me: wisemanumanah@gmail.com\n");
    scanf("%d", &user);
    printf("%d", user);
    return 0;
}