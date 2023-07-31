#include "main.h"
/**
* print_diagsums - prints the sum of the diagonals
*
* @a: pointer to the array
* @size: length/breadth of square-sized array
*
*/

void print_diagsums(int *a, int size)
{
         int i;
         int sum;

         sum = 0;
         for (i = 0; i < (size * size); i += (size + 1))
         {
                 sum += a[i];
         }
         _putchar(sum);
         _putchar(',');
         _putchar(' ');
         sum = 0;
         for (i = (size - 1); i < ((size * size) - (size - 1)); i += (size - 1))
         {
                 sum += a[i];
         }
         _putchar(sum);
}
#include <unistd.h>


/**
* _putchar - writes the character c to stdout
* @c: The character to print
*
* Return: On success 1.
* On error, -1 is returned, and errno is set appropriately.
*/
int _putchar(char c)
{
         return (write(1, &c, 1));
}