#include <stdio.h>
#include <string.h>
#include <ctype.h>

void alfabetik_siralama();

char string[999];
int uzunluk,i,j;
char compare;

int main() {
	
    printf("Bir karakter dizisi girin: ");
    gets(string);

    for(i=0;string[i]!='\0';i++)
	{
        if(string[i]=='\n')
		{
            string[i]='\0';
            break;
        }
    }
	
	alfabetik_siralama();
	
    printf("Siralanmis dizi:%s\n",string);

    uzunluk=strlen(string);

    if(uzunluk>=1)
		printf("En buyuk 1. karakter: %c\n",string[uzunluk-1]);
    if(uzunluk>=2)
		printf("En buyuk 2. karakter: %c\n",string[uzunluk-2]);
    if(uzunluk>=3)
		printf("En buyuk 3. karakter: %c\n",string[uzunluk-3]);

    return 0;
}

void alfabetik_siralama()
{
    uzunluk=strlen(string);

    for(i=0;i<uzunluk-1;i++)
	{
    	for(j=i+1;j<uzunluk;j++)
		{
            if(tolower(string[i])>tolower(string[j]))
			{
                compare=string[i];
                string[i]=string[j];
                string[j]=compare;
            }
        }
    }
}