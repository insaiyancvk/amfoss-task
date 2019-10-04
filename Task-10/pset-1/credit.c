#include <stdio.h>
#include<ctype.h>
#include <cs50.h>

int main (void)
{
    long long i=1, xa, x2;
    int adds, x2p, sum;
    do
    {
        printf("Number : ");
        scanf("%lld",&i);
    }while ( i < 0 );
    
    for ( xa = i, adds = 0; xa > 0; xa /= 100 )
        adds += xadd % 10;
    for ( x2 = i / 10, x2p = 0; x2 > 0; x2 /= 100 )
    {
        if ( 2 * (x2 % 10) > 9 )
        {
            x2p += (2 * (x2 % 10)) / 10;
            x2p += (2 * (x2 % 10)) % 10;
        }
        else
            x2p += 2 * (x2 % 10);
    }
    
    sum = adds + x2p;
    if ( sum % 10 == 0 )
    {   
        if ( (i >= 340000000000000 && i < 350000000000000) || (i >= 370000000000000 && i < 380000000000000) )
            printf("AMERICAN EXPRESS\n");
        else if ( i >= 5100000000000000 && i < 5600000000000000 )
            printf("MASTERCARD\n");
        else if ( (i >= 4000000000000 && i < 5000000000000) || (i >= 4000000000000000 && i < 5000000000000000) )
            printf("VISA\n");
        else
            printf("INVALID\n");
    }
    else
        printf("INVALID\n");

    return 0;
}

