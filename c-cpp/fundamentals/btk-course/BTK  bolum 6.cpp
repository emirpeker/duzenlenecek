#include <stdio.h>
#include <math.h>

int main(){
			/*		printf("Merhaba, Dunya!\n");
					return 0;}
		  	*/
	
	//					DEĞİŞKEN ATAMA			
			/*		int x = 5, y = 6, z = 50;
					printf("%d", x + y + z);
					printf("\n ... \n");
		
					x = y = z = 50;
					printf("%d", x + y + z);
					return 0;
			*/
	//					ARİTMETİK İŞLEMLER	
			/*		int sayi1, sayi2;
					int toplam, fark, carpim, mod;
					float bolum;
					
					printf("Lutfen iki sayi giriniz: ");
					scanf("%d%d", &sayi1, &sayi2);
					
					toplam = sayi1 + sayi2;
					fark = sayi1 - sayi2;
					carpim = sayi1 * sayi2;
					bolum = (float)sayi1 / sayi2;
					mod = sayi1 % sayi2;
					
					printf("Toplam= %d\n", toplam);
					printf("Fark= %d\n", fark);
					printf("Carpim= %d\n", carpim);
					printf("Bolum= %f\n", bolum);
					printf("Mod= %d\n", mod);
				
					return 0;
			*/
	//					HIZLI DEĞİŞKEN ATAMA, ++ OPERATÖRÜNÜN İŞLEVİ
			/*		int i = 3;
					
					i += 5; printf("%d\n",i);
					i -= 5; printf("%d\n",i);
					i *= 3; printf("%d\n",i);
					i /= 3; printf("%d\n",i);
					
					printf("\n %d\n", i++);
					printf("%d\n", i);
					printf("%d\n", ++i);
					printf("%d\n", i);
					
					return 0;	
			*/
	//						TYPECASTİNG UYGULAMASI				
			/*		int sayi1 = 17, sayi2 = 5;
					int tamsayi_bolme_sonucu, float_tamsayi_bolme_sonucu;
					float float_bolme_sonucu;
					double double_bolme_sonucu; 
					
					tamsayi_bolme_sonucu = sayi1 / sayi2;
					printf("Tamsayi Bolme Sonucu = %d\n", tamsayi_bolme_sonucu);
					float_bolme_sonucu = (float)sayi1 / sayi2;
					printf("Float Bolme Sonucu = %.20f\n", float_bolme_sonucu);
					double_bolme_sonucu = (double)sayi1 / sayi2;
					printf("Double Bolme Sonucu = %.20f\n", double_bolme_sonucu);
					float_tamsayi_bolme_sonucu = (int)float_bolme_sonucu;
					printf("Float'un Tamsayiya Donusturulmus Hali = %d\n",float_tamsayi_bolme_sonucu);
					return 0;
			*/
	//						FARKLI SAYI TİPERLİNİ YAZDIRMA				
			/*		int a=35;
					int b=0b00100011;
					int c=0x23;
					
					printf("%d\n",a);	
					printf("%d\n",b);
					printf("%d\n",c);
					return 0;
			*/	
	//						BİRİM ÇEVRİMLERİ			
			/*		float metre, cm, km;
					
					printf("Uzunlugu santimetre cinsinden giriniz: ");
					scanf("%f",&cm);
					
					metre = cm / 100.0;
					km = cm / 100000.0;
					
					printf("Metre Cinsinden Uzunluk= %.3f m\n", metre);
					printf("Kilometre Cinsinden Uzunluk= %.3f km\n", km);
					return 0;
			*/
	//						MATEMATİKSEL İŞLEMLER
	//						KUVVET ALMA
			/*		double taban, kuvvet, sonuc;
					printf("Taban Degerini Giriniz: ");
					scanf("%1lf", &taban);
					printf("Kuvvet Degerini Giriniz: ");
					scanf("%1lf", &kuvvet);
					
					sonuc= pow(taban, kuvvet);	
					printf("%.2lf ^ %.2lf = %.2lf", taban, kuvvet, sonuc);	
					return 0;
			*/
		//				KAREKÖK ALMA
			/*		double sayi, karekok;
					printf("Karekoku Hesaplanacak sayiyi giriniz: ");
					scanf("%1f", &sayi);	
					karekok = sqrt(sayi);		
					printf("%.2lf sayisinin karekoku = %.2lf", sayi, karekok);
					return 0;
			*/		
		//					BASİT/BİLEŞİK FAİZ
			/*		float ana_para, zaman, faiz_orani, basit_faiz_miktari, bilesik_faiz_miktari;
					
					printf("Ana Para miktarini giriniz: ");
					scanf("%f", &ana_para);
					printf("Zamani giriniz: ");
					scanf("%f", &zaman);
					printf("Faiz oranini giriniz: ");
					scanf("%f", &faiz_orani);
					
					basit_faiz_miktari = (ana_para * zaman * faiz_orani) / 100;	
					printf("Basit Faiz Miktari: %f \n", basit_faiz_miktari);
					
					bilesik_faiz_miktari = ana_para * (pow((1 + faiz_orani/100), zaman));
					printf("Bilesik Faiz Miktari: %f", bilesik_faiz_miktari);
					
					
					
					return 0;		
			*/		
		//					GETCHAR ve PUTCHAR İŞLEMLERİ
			/*		char ogrenci_notu;
					printf("Ogrenci notunu giriniz: ");
					ogrenci_notu = getchar();
					putchar(ogrenci_notu);
					return 0;
			*/		
		//					DİKDÖRTGEN ALAN VE ÇEVRE
			/*	float boy, en, alan, cevre;
				printf("Dikdortgenin uzunlugunu giriniz: ");
				scanf("%f", &boy);
				printf("Dikdortgenin genisligini giriniz: ");
				scanf("%f", &en);
				
				cevre = 2 * (en+boy);
				printf("Dikdotgenin cevresi: %f birimdir. \n", cevre);
				
				alan = en * boy;
				printf("Dikdotgenin alani: %f birimdir. \n", alan);
				return 0;
			*/		
	//					DAİRE/ÇEMBER İŞLEMLERİ
			/*	float cap, yaricap, cevre, alan;
				printf("Cemberin/Dairenin yaricapini giriniz: ");
				scanf("%f", &yaricap);
				cap= 2 * yaricap;
				cevre= 2 * M_PI * yaricap;
				alan= M_PI	 * (yaricap*yaricap);
				
				printf("Cember/Dairenin capi= %.2f birimdir. \n", cap);
				printf("Cember/Dairenin cevresi= %.2f birimdir. \n", cevre);
				printf("Cember/Dairenin alani= %.2f birimdir. \n", alan);
				
				return 0;
			*/		
					
					
					
							
			}