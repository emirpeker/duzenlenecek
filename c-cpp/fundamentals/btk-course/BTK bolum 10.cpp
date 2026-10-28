#include <stdio.h>
#include <math.h>

int main(){
	//				İF KOMUTU
		/*	int sayi1, sayi2;
			
			printf("Lutfen iki sayi degeri giriniz:");
			scanf("%d%d", &sayi1, &sayi2);
			
			if(sayi1>sayi2) {
								printf("%d daha buyuktur", sayi1);	
							}
			if (sayi2>sayi1){
								printf("%d daha buyuktur", sayi2);
							}
			if (sayi2==sayi1){
								printf("iki sayi esittir");
							}
			return 0;
		*/
	//			ELSE İF KOMUTU
		/*	int sayi;
			printf("Lutfen bir sayi giriniz: ");
			scanf("%d", &sayi);
			
			if(sayi>0){
						printf("Sayi pozitiftir");
				}
			else if(sayi<0){
							printf("Sayi negatiftir");
			}
			else {
					printf("Sayi 0 dir");				
				}
		*/
	//			İF KOMUTLARI AYNI PROBLEM FARKLI ÇÖZÜMLER
		/*	int sayi1, sayi2, sayi3, maksimum;
			printf("Uc sayi giriniz:");
			scanf("%d%d%d",&sayi1,&sayi2,&sayi3);
			
			if(sayi1>sayi2){
							if(sayi1>sayi3){
											maksimum =sayi1;
											}
							else{
									maksimum = sayi3;	
								}
							}
			else {
					if(sayi2>sayi3){
						maksimum = sayi2;
									}
					else{
						maksimum=sayi3;
					}
				}
			printf("3 sayi icin en buyuk deger = %d", maksimum);			
		*/
		
		/*	int sayi1, sayi2, sayi3, maksimum;
			printf("Uc sayi giriniz:");
			scanf("%d%d%d",&sayi1,&sayi2,&sayi3);
				
			if((sayi1>sayi2) && (sayi1>sayi3)){
											maksimum=sayi1;
											}
			else if((sayi2>sayi1) && (sayi2>sayi3)){
													maksimum=sayi2;
													}								
			else if((sayi3>sayi1) && (sayi3>sayi2)){
												maksimum=sayi3;
													}
			printf("3 sayi icin en buyuk deger = %d", maksimum);														
		*/
		
		/*	int sayi1, sayi2, sayi3, maksimum;
			printf("Uc sayi giriniz:");
			scanf("%d%d%d",&sayi1,&sayi2,&sayi3);
			
			if((sayi1>sayi2) && (sayi1>sayi3)){
											maksimum=sayi1;
											}
			else if(sayi2>sayi3){
									maksimum=sayi2;
									}
			else{
				maksimum=sayi3;
				}
			printf("3 sayi icin en buyuk deger = %d", maksimum);
			
		*/
		
//		------------------------------------------------
	//			İF ELSE UYGULAMALARI
		/*	int maliyet, satis_bedeli, kar_zarar;
			
			printf("Maliyet bedelini giriniz: ");
			scanf("%d", &maliyet);
			printf("Satis bedelini giriniz: ");
			scanf("%d", &satis_bedeli);
			
			if(satis_bedeli>maliyet){
									kar_zarar = satis_bedeli - maliyet;
									printf("Kar = %d", kar_zarar);
									}
			else if(satis_bedeli<maliyet){
											kar_zarar = maliyet - satis_bedeli;
											printf("Zarar = %d", kar_zarar);
										}
			else{
				printf("Kar veya zarar edilmemistir.");
				}
		*/
	//				ARTIK YIL HESAPLAMA	
		/*	int yil;
			printf("Yil degerini giriniz: ");
			scanf("%d", &yil);
			
			if(((yil%4==0) && (yil%100!=0)) || (yil%400==0)){
															printf("Yil artik yildir.");				
														}
			else{
				printf("Yil artik yil degildir.");
				}
		*/
	//				KÖK BULMA İF İLE	
		/*	float a,b,c;
			float kok1, kok2, imajiner;
			float diskriminant;
			
			printf("(aX^2 + bX + c) seklindeki ikinci dereceden denklemin a,b ve c katsayilarini girin: ");
			scanf("%f%f%f", &a, &b, &c);
			
			diskriminant = (b * b) - (4 * a * c);
			
			if(diskriminant>0){
								kok1=(-b + sqrt(diskriminant))/(2*a);
								kok1=(-b - sqrt(diskriminant))/(2*a);
								printf("iki adet ayrik ve gercel kok vardır: %.2f ve %.2f", kok1, kok2);
							}		
			else if(diskriminant==0){
										kok1=kok2= -b / (2*a);
										printf("Birbirine esit iki adet gercel kok vardır: %.2f", kok1);
									}
			else if(diskriminant<0){
									kok1=kok2= -b / (2*a);
									imajiner = sqrt(-diskriminant) / (2*a);	
									printf("iki adet ayrik ve karmasik kok vardir: %.2f + i%.2f ve %.2f - i%.2f", kok1, imajiner, kok2, imajiner);			
									}
		*/
	//				İF KARAKTER UYGULAMASI
	    /*	char karakter;
			printf("Lutfen bir karakter giirinz: ");
			scanf("%c", &karakter);
			
			if((karakter>='a' && karakter <='z') || (karakter >= 'A' && karakter<= 'Z'))
	 		printf("Alfabetik bir karakter girdiniz.");
	 		else
	 		printf("Alfabetik olmayan bir karakter girdiniz.");
		*/	}