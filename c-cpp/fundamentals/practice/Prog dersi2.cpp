#include <stdio.h>
#include <cstring>

int main()
{
/*	char dizi[50];
	int i;
	printf("Metni giriniz: \n");
	gets(dizi);
	
	printf("Karakterleri tek tek yazdir\n");
	for(i=0;i<=dizi[i];i++)
	{
		printf("%c\n",dizi[i]);
	}
	printf("\nTum karakterleri yazdir\n");
	printf(dizi);
	printf("\n");
	*/
/*	char dizi[50];
	int i;
	printf("Lutfen metni gir:");
	gets(dizi);
	
	printf("Uzunluk:%d",strlen(dizi));
	printf("\n");
	*/
/*	char metin1[50],metin2[50];
	printf("Lutfen 1.metni giriniz: ");
	gets(metin1);
	printf("Lutfen 2.metni giriniz: ");
	gets(metin2);
	
	strcat(metin1,metin2);
	printf("\nBirlestirilmis metin: ");
	printf(metin1);
	printf("\n");
	*/
	#include <stdio.h>



char karakter;

//klavyeden bir karakter oku ve enter tusunu bekle//

printf("bir karakter giriniz ve enter tusuna basiniz:");

karakter=getchar();

printf("girilen karakter:");

//okunan karakteri ekrana yazdir//

putchar (karakter);

return 0;


}