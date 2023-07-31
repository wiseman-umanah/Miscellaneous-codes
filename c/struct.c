#include <string.h>
#include <stdio.h>
#include "dog.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */

dog_t *new_dog(char *name, float age, char *owner);
void free_dog(dog_t *d);

int main(void)
{
    dog_t *my_dog;

    my_dog = new_dog("Bingo", 17, "Deborah");
    printf("My name is %s, and I am %.1fyears, and my owner is %s - Woof!\n", my_dog->name, my_dog->age, my_dog->owner);
    free_dog(my_dog);
    return (0);
}

dog_t *new_dog(char *name, float age, char *owner)
{
    dog_t *doggy;
    size_t namelen, ownerlen;

    namelen = strlen(name) + 1;
    ownerlen = strlen(owner) + 1;
    doggy = NULL;
    doggy = malloc(sizeof(struct dog));
    if (doggy == NULL)
    {
        free(doggy);
        return(NULL);
    }
    else
    {
        doggy->name = malloc(namelen);
        doggy->owner = malloc(ownerlen);
        
        if (doggy->name == NULL || doggy->owner == NULL)
        {
            free(doggy->name);
            free(doggy->owner);
            free(doggy);
            return (NULL);
        }
        strcpy(doggy->name, name);
        strcpy(doggy->owner, owner);
        doggy->age = age;

        return(doggy);
    }

}

void free_dog(dog_t *d)
{
    free(d->name);
    free(d->owner);
    free(d);
}