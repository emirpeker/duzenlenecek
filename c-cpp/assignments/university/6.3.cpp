#include <stdio.h>
#include <stdlib.h>

int kisi,i;
int puan[40];

void OrtalamaHesapla();
void EnYuksekNot();
void GecenOgrenciler();

int main()
{	
	printf("Siniftaki ogrenci sayisini girin:");
	scanf("%d",&kisi);
	
	for(i=0;i<kisi;i++)
	{
		printf("Ogrenci %d'in notunu girin:",i+1);
		scanf("%d",&puan[i]);
	}
	OrtalamaHesapla();
	EnYuksekNot();
	GecenOgrenciler();
	return 0;
}
void OrtalamaHesapla()
{
	int topla;
	for(i=0;i<kisi;i++)
		 topla+=puan[i];
	float ortalama=topla/kisi;
	printf("\nSinif Not Ortalamasi: %.1f",ortalama);
}
void EnYuksekNot()
{
	int max=0;
	for(i=0;i<kisi;i++)
	{
		if(puan[i]>max)
			max=puan[i];
	}
	printf("\nEn Yuksek Not: %d\n",max);
}
void GecenOgrenciler()
{
	int gecmeNot=60;
	printf("Gecme Notu: %d",gecmeNot);
	printf("\nGecen Ogrencilerin Notlari:");
	for(i=0;i<kisi;i++)
	{
		if(puan[i]>=gecmeNot)
			printf(" %d",puan[i]);		
	}	
}