#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>


int main()

{
/*  //büyük ünlü uyumuna uyuyor veya uymuyor
char kelime[15];

int uzunluk,i,kalinSesli=0,inceSesli=0;

printf("Bir kelime girin: ");

scanf("%s",kelime);

uzunluk=strlen(kelime);

for(i=0;i<uzunluk;i++){

if(kelime[i]=='a'||kelime[i]=='o'||kelime[i]=='u'||kelime[i]=='ı'){

kalinSesli+=1; }

if(kelime[i]=='e'||kelime[i]=='i'||kelime[i]=='ü'||kelime[i]=='ö'){

inceSesli+=1; } }

if(kalinSesli==0||inceSesli==0){

printf("%s Kelimesi Buyuk Unlu Uyumuna Uyuyor.",kelime);}

else{

printf("%s Kelimesi Buyuk Unlu Uyumuna Uymuyor.",kelime);}
*/
/*
//Kaç tane a harfi olduüu
char kelime[50];

char ara='a';

int i,adet=0;

printf("Lutfen bir kelime girin:");

scanf("%s",kelime);

for(i=0; kelime[i]!='\0';i++)

{ if (kelime[i]==ara) adet++;}

printf(" a degeri %d tane vardir", adet);

return 0;
*/
	//ne bastırır
int a,i;

char sinif[13][20]=

{"zeynep","fehime","celal","yaren","arda","yusuf","taha","elif","ibrahim","selin","emre","Haktan","Hayri"};

printf("%c \n",sinif[1][0]);

for ( i = 0; i < 13; i++) {

printf("%s \n",sinif[i]);}

/* //kaç tane kucuk buyyuk ve rakam kullanılmış
char metin [100];

int i, kucukharf=0, buyukharf=0, rakam=0;

printf("\n bir kelime giriniz:");

scanf("%s",metin);

for(i=0; metin[i]!= '\0'; i++) {

if(isdigit(metin[i]))

rakam++;

if(islower(metin[i]))

kucukharf++;

else if (isupper(metin[i]))

buyukharf++;

}

printf("%d tane kucuk harf %d tane buyuk harf, %d tane rakam",kucukharf,buyukharf,rakam);
*/
/* //cumle gir sonra kontrol edilecek karakteri gir bak
int i,j,k=0,n=0,sayac=0,a,s1=0,s2=0;

char cumle[100]; char kontrol;

printf("cumleyi giriniz:");

gets(cumle);

printf("kontrol edilecek harf:");

kontrol=getchar();

printf("\n");

for(i=0;cumle[i]!='\0';i++)

sayac++;

for(i=0;i<sayac;i++){

s2=s1;

for(;cumle[i]!=' '&& i<sayac;i++){

if(cumle[i]==kontrol)

k++;

s1++;

}

if(cumle[i]==' ')

s1++;

if(k>n){

j=s2;n=k; a=i;

}

k=0;

}

if(n>0){

printf("%c karakterini en cok tekrar edildigi kelime ==> ",kontrol);

for(;j<a;j++)

printf("%c", cumle[j]);

printf(" kelimesinde %c karakteri %d kez geciyor.",kontrol,n);

}else

printf("%c karakteri hicbir kelimede bulunmamaktadir.",kontrol);
*/
/*	char dizi1[5],dizi2[5];
	int i,gecici;

	printf("Dizi1 degerlerini gir:");

	for(i=0;i<5;i++)
		scanf("%d",&dizi1[i]);

	for(int i=0;i<5;i++)
	{
		for(int j=i+1;j<5;j++)
		{
			if(dizi1[j]<dizi1[i])
			{
				gecici=dizi1[i];
				dizi1[i]=dizi1[j];
				dizi1[j]=gecici;
			}
		}
	}
	printf("\nSiralanmis dizi: ");

	for(i=0;i<5;i++)
		printf("%d ",dizi1[i]);

	printf("\nDizi2 degerlerini gir:");
	for(i=0;i<5;i++)
		scanf("%d",&dizi2[i]);
	strcat(dizi1,dizi2);
	*/
	return 0;

}
