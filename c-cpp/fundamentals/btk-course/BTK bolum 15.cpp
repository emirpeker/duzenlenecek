#include <Stdio.h>
#include <Stdlib.h>//2. uygulama

#define BUYUK_SAYI 1000000 //2.uygulama

int belirliislemgerceklestir(int girdi){//2. 3. uygulama
	return(girdi<BUYUK_SAYI);
	
}

int g;//4.uygulama

int a=20;//5.uygulama

int baziislemlergerceklestir(int a,int b){//5.uygulama
	printf("a degiskeninin baziislemlergerceklestir() fonk.u icindeki giris degeri= %d\n",a);
	printf("b degiskeninin baziislemlergerceklestir() fonk.u icindeki giris degeri= %d\n",b);
	
	a*=12;
	b+=5;
	
	printf("a degiskeninin baziislemlergerceklestir() fonk.u icindeki sonraki degeri= %d\n",a);
	printf("b degiskeninin baziislemlergerceklestir() fonk.u icindeki sonraki degeri= %d\n",b);
	return a+b;
}

int main(){
/*	const int dakikasayisi =60;
	const float PI=3.14;
	
	printf("%d\n",dakikasayisi);
	printf("%f\n",PI);
	
	//PI=PI+5;  //SATIR AÇILIRSA HATA
*/
	
/*	int ilk_degisken=20,ikinci_degisken=25,sonuc1,sonuc2;
	const int BASKA_BIR_BUYUK_SAYI=1000000;
	
	printf("Buyuk sayi: %d\n",BUYUK_SAYI);
	
	sonuc1=(ilk_degisken<BUYUK_SAYI);
	printf("Sonuc1 : %d\n",sonuc1);
	
	sonuc2=(ikinci_degisken<BUYUK_SAYI);
	printf("Sonuc2: %d\n",sonuc2);
	
	#undef BUYUK_SAYI
	#define BUYUK_SAYI 30000000
	printf("Buyuk sayi:%d\n",BUYUK_SAYI);
*/	
/*	int ilk_degisken=20,ikinci_degisken=25,sonuc1,sonuc2;
	const int BASKA_BIR_BUYUK_SAYI=1000000;
	int sonuc3;
	
	printf("Buyuk sayi: %d\n",BUYUK_SAYI);
	
	sonuc1=(ilk_degisken<BUYUK_SAYI);
	printf("Sonuc1 : %d\n",sonuc1);
	
	sonuc2=(ikinci_degisken<BUYUK_SAYI);
	printf("Sonuc2: %d\n",sonuc2);
	
	#undef BUYUK_SAYI
	#define BUYUK_SAYI 30000000
	printf("Buyuk sayi:%d\n",BUYUK_SAYI);
	
	sonuc3=belirliislemgerceklestir(30);
	printf("Sonuc3: %d\n",sonuc3);

*/
	
/*	int a,b;
	a=10,b=20,g=a+b;
	
	printf("a= %d ,b= %d, g=%d \n",a,b,g);
	
*/
	
	int a=10,b=20,c=0;
	printf("a degiskeninin main() icindeki degeri= %d\n",a);	
	printf("b degiskeninin main() icindeki degeri= %d\n",b);
	
	c=baziislemlergerceklestir(a,b);
	printf("c degiskeninin main() icindeki degeri= %d\n",c);
	
	printf("a degiskeninin main() icindeki degeri= %d\n",a);
	printf("b degiskeninin main() icindeki degeri= %d\n",b);

	return 0;

}