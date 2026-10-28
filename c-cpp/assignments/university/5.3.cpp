#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


int main() {
    char string[999];
    int i,toplam=0;

    printf("Bir string girin: ");
    gets(string);

    for (i=0;string[i]!='\0';i++)
	{
        if (isdigit(string[i]))
            toplam+=string[i]-'0';
    }

    printf("Stringdeki rakamlarin toplami: %d\n",toplam);

    return 0;
}