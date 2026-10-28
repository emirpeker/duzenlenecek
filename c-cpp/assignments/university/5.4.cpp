#include <stdio.h>
#include <stdlib.h>

int main()
{
	char string[999];
	int i;
	
    printf("Bir string girin: ");
    gets(string);
    
    for(i=0;string[i]!='\0';i++)
	{
        if(string[i]=='\n')
		{
            string[i]='\0';
            break;
        }
        
        if(string[i]>='a' && string[i]<='z')
            string[i]=((string[i]-'a'+3)%26)+'a'; //%26 alfabenin başına dönmek için dönmezsek [ gibi karakterler olacaktır şifrede.
            
		else if(string[i]>='A' && string[i]<='Z')
            string[i]=((string[i]-'A'+3)%26)+'A'; //%26 alfabenin başına dönmek için dönmezsek [ gibi karakterler olacaktır şifrede.
    }
    printf("Sifrelenmis string: %s\n",string);
	return 0;
}