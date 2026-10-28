#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
void rastgele_dizi(int *dizi,int boyut)//rastgele sayılarla dizi oluşturan fonksiyon
{
    srand(time(NULL));//rastgele sayı üretirken her defasında farklı sayı vermesi için zaman kullanıldı
    for(int i=0;i<boyut;i++)
        dizi[i]=rand()%1000;//0 ile 999 arasında rastgele sayılar seçer
}

int en_buyuk(int *dizi,int boyut,int *EnBuyuk, int *IkinciEnBuyuk)//en büyük ve ikinci en büyük sayıyı bulan fonksiyon
{
    *EnBuyuk= *IkinciEnBuyuk=-1;
    for(int i=0;i<boyut;i++)
	{
        if(dizi[i]>*EnBuyuk)
		{
            *IkinciEnBuyuk= *EnBuyuk;
            *EnBuyuk=dizi[i];
        } 
		else if(dizi[i]> *IkinciEnBuyuk&&dizi[i]!= *EnBuyuk)
            *IkinciEnBuyuk=dizi[i];
    }
}

int en_kucuk(int *dizi,int boyut)//en küçük sayıyı bulan fonksiyon
{
    int EnKucuk=dizi[0];
    for(int i=1;i<boyut;i++)
        if(dizi[i]<EnKucuk)
            EnKucuk=dizi[i];
    return EnKucuk;
}
double standart_sapma(int *dizi,int boyut)// Standart sapma hesaplayan fonksiyon
{
	double toplam,ortalama,farkToplam;
	for(int i=0;i<boyut;i++)
		toplam+= dizi[i];
	
	ortalama=toplam/boyut;	
	
	for(int i=0;i<boyut;i++)
		farkToplam+=(dizi[i]-ortalama)*(dizi[i]-ortalama);
	
	double karekok=farkToplam/boyut;
	karekok=sqrt(karekok);
	return karekok;		
}

int main()
{
    int dizi[4];
    int EnBuyuk,IkinciEnBuyuk,EnKucuk;
    double standartS;
    
    rastgele_dizi(dizi,4);//diziyi oluşturur
    
    en_buyuk(dizi,4,&EnBuyuk,&IkinciEnBuyuk);//en büyük ve ikinci en büyük elemanı bulur
    
    EnKucuk=en_kucuk(dizi,4);//en küçük elemanı bulur
    
    standartS=standart_sapma(dizi,4);//standart sapmayı hesaplar
    
    printf("Dizi Elemanlari: ");
    for(int i=0;i<4;i++)
        printf("%d ",dizi[i]);
    printf("\n");
    
    printf("En buyuk: %d\n",EnBuyuk);
    printf("Ikinci en buyuk: %d\n",IkinciEnBuyuk);
    printf("En kucuk: %d\n",EnKucuk);
    printf("Standart Sapma: %.2lf\n",standartS);
    return 0;
}