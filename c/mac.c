#include <stdio.h>
#include "dog.h"
#include <stddef.h>

 /**
 * print_dog - prints the details of the dog
 *
 * @d: pointer to dog
 */
#include <stdlib.h>
/**
 * main - check the code .
 *
 * Return: Always 0.
 */

void print_dog(struct dog *d);

int main(void)
{
	struct dog my_dog;

	my_dog.name = NULL;
	my_dog.age = .0f;
	my_dog.owner = NULL;
	print_dog(NULL);
	return (0);
}
void print_dog(struct dog *d)
{
         if (d == NULL)
                return;
         else
         {
                 if (d->name == NULL)
                         puts("Name: (nil)");
                 else
                         printf("Name: %s\n", d->name);
                 printf("Age: %f\n", d->age);
                 if (d->owner == NULL)
                         printf("Owner: (nil)");
                 else
                         printf("Owner: %s\n", d->owner);
          }
 }         