#include <stdio.h>
#include <string.h>

void sesliHarf(char metin[],int i,int sayac[])
{
    if(metin[i]=='\0')
        return;

    if(metin[i]=='a' || metin[i]=='A')
		sayac[0]++;
    if(metin[i]=='e' || metin[i]=='E')
		sayac[1]++;
    if(metin[i]=='i' || metin[i]=='I')
		sayac[2]++;
    if(metin[i]=='o' || metin[i]=='O')
		sayac[3]++;
    if(metin[i]=='u' || metin[i]=='U')
		sayac[4]++;

    sesliHarf(metin,i+1,sayac);
}

int main()
{
    char metin[100];
    int sayac[5]={0};

    printf("Bir metin giriniz: ");
    fgets(metin,sizeof(metin),stdin);

     for(int j=0;j<100;j++)
    {
        if(metin[j]=='\n')
        {
            metin[j]='\0';
            break;
        }
    }

    sesliHarf(metin,0,sayac);

    printf("Sesli harflerin sayilari:\n");
    printf("A: %d\n",sayac[0]);
    printf("E: %d\n",sayac[1]);
    printf("I: %d\n",sayac[2]);
    printf("O: %d\n",sayac[3]);
    printf("U: %d\n",sayac[4]);

    return 0;
}
