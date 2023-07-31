#include <stdio.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int is_prime_number(int n);
int checker(int n, int prime);

int main(void)
{
    int r;

    r = is_prime_number(1);
    printf("%d\n", r);
    r = is_prime_number(1024);
    printf("%d\n", r);
    r = is_prime_number(16);
    printf("%d\n", r);
    r = is_prime_number(17);
    printf("%d\n", r);
    r = is_prime_number(25);
    printf("%d\n", r);
    r = is_prime_number(-1);
    printf("%d\n", r);
    r = is_prime_number(113);
    printf("%d\n", r);
    r = is_prime_number(7919);
    printf("%d\n", r);
    return (0);
}
int is_prime_number(int n)
{
    if (n <= 1)
        return 0;
    
    checker(n, 2);
}

int checker(int n, int prime)
{
    if (prime < n)
    {
        if (n % prime == 0)
            return 0;
        checker(n, prime + 1);
    }
    else 
        return 1;    
}