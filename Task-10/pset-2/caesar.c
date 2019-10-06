#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

 int main()
 {
    {
        char code[100];
        scanf("%[^\n]%*c",code);
        
        for (int i = 0, n = strlen(code); i < n; i++)
            {
                if islower(code[i])
                    printf("%c", (((code[i] + 1) - 97) % 26) + 97);
                else if isupper(code[i])
                    printf("%c", (((code[i] + 1) - 65) % 26) + 65);
                else
                    printf("%c", code[i]);
            }
            printf("\n");
            return 0;
    }
 }

