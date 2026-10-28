#include <Stdio.h>
#include <Stdlib.h>

int main()
{
	float odenecekFatura,eskiBirimFiyat,yeniBirimFiyat;
	float enflasyon,eskiAbonelikUcreti,yeniAbonelikUcreti;
	int yeniOkuma,eskiOkuma,toplamHarcananElektrik;
	
	printf("Enflasyon oranini girin: ");
	scanf("%f",&enflasyon);
	printf("Onceki aya ait birim fiyat miktarini girin: ");
	scanf("%f",&eskiBirimFiyat);
	printf("Onceki aya ait abonelik ucretini girin: ");
	scanf("%f",&eskiAbonelikUcreti);
	printf("Bir onceki aya ait okuma degerini girin: ");
	scanf("%d",&eskiOkuma);	
	printf("Bu aya ait okuma degerini girin: ");
	scanf("%d",&yeniOkuma);
				
	yeniBirimFiyat = eskiBirimFiyat * (1 + enflasyon / 100);
	yeniAbonelikUcreti= eskiAbonelikUcreti * (1 + enflasyon / 100);
	toplamHarcananElektrik= yeniOkuma - eskiOkuma;
	
	odenecekFatura = toplamHarcananElektrik * yeniBirimFiyat + yeniAbonelikUcreti;
	
	printf("Toplam fatura miktariniz= %f",odenecekFatura);
	
	return 0;
}