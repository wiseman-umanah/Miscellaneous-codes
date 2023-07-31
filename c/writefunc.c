#include <unistd.h>

int _putchar(char *c)
{
    return(write(1, c, 10));
    
}

int main()
{
    char *c  = "Hell";

    _putchar(c);
}