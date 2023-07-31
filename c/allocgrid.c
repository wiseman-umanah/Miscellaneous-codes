#include <stdio.h>
#include <stdlib.h>

/**
 * print_grid - prints a grid of integers
 * @grid: the address of the two dimensional grid
 * @width: width of the grid
 * @height: height of the grid
 *
 * Return: Nothing.
 */
void print_grid(int **grid, int width, int height)
{
    int w;
    int h;

    h = 0;
    while (h < height)
    {
        w = 0;
        while (w < width)
        {
            printf("%d ", grid[h][w]);
            w++;
        }
        printf("\n");
        h++;
    }   
}

int **alloc_grid(int width, int height)
{
    int **num;
    int i;
    int j;

    num = NULL;
    if (width <= 0 || height <= 0)
    {
        return (num);
    }
    else
    {
        num = (int **)malloc(height * sizeof(int*));
        if (num == NULL)
        {
            return (num);
        }
        else 
        {
            for (i = 0; i < height; i++)
            {
                num[i] = (int*) malloc(width * sizeof(int));
            }
            for (i = 0; i < height; i++)
            {
                for (j = 0; j < width; j++)
                {
                    num[i][j] = 0;
                }
            }
            return (num);
        }
    }
}

int main(void)
{
    int **grid;

    grid = alloc_grid(0, 0);
    if (grid == NULL)
    {
        puts("Not what you expected");
        return (1);
    }
    print_grid(grid, 6, 4);
    printf("\n");
    grid[0][3] = 98;
    grid[3][4] = 402;
    print_grid(grid, 6, 4);
    return (0);
}