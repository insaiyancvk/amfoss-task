#include <stdio.h>
#include <cs50.h>

int main(void)
{
   int height;

    do
    {
        printf("Please specify the height of the pyramid: ");
        scanf("%d",&height);
    }
    while (height < 0 || height > 23);

    for (int line = 0; line < height; line++)
    {
        for (int spaces = height - line; spaces > 1; spaces--)
        {
            printf(" ");
        }
        for (int hashes = 0; hashes < line + 1; hashes++)
        {
            printf("#");
        }
        printf(" ");
        for (int hashes = 0; hashes < line + 1; hashes++)
        {
            printf("#");
        }
        printf("\n");
    }
}

