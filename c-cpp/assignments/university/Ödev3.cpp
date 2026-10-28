//#include <Stdio.h>

//int main(){
	/*	int satirsayisi;
		int sayi = 1;  
		printf("Satir sayisini giriniz: ");
    	scanf("%d", &satirsayisi);
    	for (int m = 1; m <= satirsayisi; m++) {
        		for (int n = 1; n <= m; n++) {
            		printf("%d ", sayi);  
            		sayi++;               
        }
        printf("\n");  
    } 
    */
	
	/*int sayi, yuzler, onlar, birler, toplam;
    printf("Uc basamakli bir sayi giriniz: ");
    scanf("%d", &sayi);

    if (sayi < 100 || sayi > 999) {printf("Lutfen uc basamakli bir sayi giriniz.\n");
        						   return 0; }
    yuzler = sayi / 100;         
    onlar = (sayi / 10) % 10;    
    birler = sayi % 10;         

    toplam = (yuzler * yuzler * yuzler) + (onlar * onlar * onlar) + (birler * birler * birler);

    if (toplam == sayi) 
        printf("%d bir Armstrong sayisidir.\n", sayi);
     else 
        printf("%d bir Armstrong sayisi degildir.\n", sayi);
    */
	
	/*int yas;
	
	printf("Yasinizi giriniz: ");
	scanf("%d", &yas);
	
	if(yas>=1 && yas<18 )
	printf("COCUK k1ategorisindesiniz.");
	else if(yas>=18 && yas<30 )
	printf("GENC kategorisindesiniz.");	
	else if(yas>=30 && yas<50 )
	printf("ORTA YAS kategorisindesiniz.");
	else if(yas>=50 && yas<=95 )
	printf("YASLI kategorisindesiniz.");
	else
	printf("Girilen yas tanimli degildir!");
	*/
	
	
/*	char karakter;
    printf("Bir karakter giriniz: ");
    scanf("%c", &karakter);

    if (karakter >= 'A' && karakter <= 'Z') 
        printf("Girdiginiz karakter BUYUK HARFtir.");
     else if (karakter >= 'a' && karakter <= 'z')
        printf("Girdiginiz karakter KUCUK HARFtir.");
     else if (karakter >= '0' && karakter <= '9') 
        printf("Girdiginiz karakter bir SAYIdir.");
     else 
        printf("Girdiginiz karakter OZEL KARAKTERdir.");
     return 0;
*/
/*#include <stdio.h>

// Faktöriyel hesaplama fonksiyonu
long long faktoriyel(int n) {
    long long sonuc = 1;
    for (int i = 1; i <= n; i++) {
        sonuc *= i;
    }
    return sonuc;
}

// Üs alma fonksiyonu (x^n)
double us_al(double x, int n) {
    double sonuc = 1.0;
    for (int i = 0; i < n; i++) {
        sonuc *= x;
    }
    return sonuc;
}

// e^x fonksiyonu hesaplama
double hesapla_e_ust_x(double x) {
    double terimler[100];
    double sonuc = 1.0; // İlk terim 1
    double terim = 1.0; // İlk terim 1

    for (int i = 1; i < 100; i++) {
        terim *= x / i; // Bir sonraki terim için güncelleme
        terimler[i] = terim;
        sonuc += terimler[i];
    }
    return sonuc;
}
int main() {
    double x;

    printf("Bir X değeri girin: ");
    scanf("%lf", &x);

    double sonuc_e_ust_x = hesapla_e_ust_x(x);
    printf("e^%.2f yaklaşık değeri: %.6f\n", x, sonuc_e_ust_x);
        return 0;
}
*/
#include <Stdio.h>
#include <Math.h>
#include <Stdlib.h>
int main(){
		int x;
		double e[100],sin[100],cos[100];
		double etoplam=0.0,stoplam=0.0,ctoplam=0.0;
		
		printf("Bir X degeri giriniz: ");
		scanf("%d",&x);
		
		for(int i=0;i<100;i++){
				double bol=1.0;
					for(int k=1;k<i;k++)
						bol= bol*k;
							
			e[i]=1+x+(x^i)/bol;
			etoplam+=e[i];	
		}
		
		printf("e^%.2d =%.5f \n",x,etoplam);
		return 0;
}