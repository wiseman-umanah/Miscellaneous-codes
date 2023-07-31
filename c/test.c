#include <stdio.h>

int main()
{
    long long int i;
    long long int j;
    long long int ans;

    i = 612852475143;
    ans = 1;

    while (i % 2 == 0)
    {
        i /= 2;
        ans = 2;
    }

    for (j = 3; j <= i; j += 2)
    {
        while (i % j == 0)
        {
            i /= j;
            ans = j;
        }
    }

    printf("%lld", ans);
    return 0;
}