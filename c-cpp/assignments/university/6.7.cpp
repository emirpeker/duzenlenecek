#include <stdio.h>

int main()
{
	const int sinir=100;
    char string[sinir]="{[()]}";
    char kontrol[sinir],i;
    int ust=-1;
    int denge=1;

    printf("Bir string girin: ");
    fgets(string,sizeof(string),stdin);

    for(i=0;string[i]!='\0';i++)
	{
        char karakter=string[i];
        if(karakter=='(' || karakter=='{' || karakter=='[')
            kontrol[++ust]=karakter;
        else if(karakter==')' || karakter=='}' || karakter==']')
		{
            if(ust==-1)
			{
                denge=0;
                break;
            }
            char acik=kontrol[ust--];
            if((karakter==')' && acik!='(') || (karakter=='}' && acik!='{') || (karakter==']' && acik!='['))
			{
                denge=0;
                break;
            }
        }
    }
    if(denge && ust==-1)
        printf("Parantezler dengede.\n");
	else
        printf("Parantezler dengesiz.\n");

    return 0;
}