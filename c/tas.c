#include <stdio.h>

int main()
{
        int a[2][2] = {
                        {2,3},
                        {3,2}
        };
        int b[2][2] = {
                        {3,4},
                        {2,3}
        };
        int c[2][2];

        int  j, k, i, sum;
        
        for (i = 0; i < 2; i++)
        {
                for (j = 0; j < 2; j++)
                {
                        sum = 0;
                        for (k = 0; k < 2; k++)
                        {
                                sum += a[i][k] * b[k][j];
                                c[i][j] = sum;
                        }
                }
        }

        for (j = 0; j < 2; j++)
        {
                for (k = 0; k < 2; k++)
                {
                        printf("%d ", c[j][k]);
                }
                putchar('\n');
        }

        return 0;
}