#include <stdio.h>
#include <stdlib.h>
/*
int main()
{
	//İLK ÖRNEK
	int kutle[5] = {5,10,15,20,25}; //5 elemanlı bir dizi tanımladık
	int *p; //Pointer tanımladık
	
	p=kutle; //Pointer'a dizinin ilk elemanının adresini atadık
	
	printf("*p degeri = %d\n",*p); //kutle dizisinin ilk elemanını(5) yazdırır
	printf("*(p+1) degeri = %d\n",*(p+1)); //*(p+1) ile kutle dizisinin ikinci elemanını(10) yazdırır
	printf("*(p+2) degeri = %d\n",*(p+2)); //*(p+2) ile kutle dizisinin üçüncü elemanını(15) yazdırır
	printf("*(p+3) degeri = %d\n",*(p+3)); //*(p+3) ile kutle dizisinin dördüncü elemanını(20) yazdırır
	printf("*(p+4) degeri = %d\n",*(p+4)); //*(p+4) ile kutle dizisinin son elemanını(25) yazdırır
	return 0;
}
*/
/*
int main()
{	//ÖRNEK 1
	int i;
	int b[]={10,20,30,40};//4 elemanlı bir dizi tanımladık

	int *pb=b;// pb pointer'ına b dizisinin başlangıç adresini atadık
	
	printf("YONTEM 1: DIZI INDISLERI\n");
	for(i=0;i<=3;i++)
		printf("b[%d]:\t%d\n",i,b[i]);//Diziye doğrudan indis kullanılarak erişim
	printf("\nYONTEM 2: ISARETCI OFFSET \n");
	for(i=0;i<=3;i++)
		printf("*(pb + %d):\t%d\n",i,*(pb + i));//pb pointer adresine i eklenerek elemanlara erişim
	printf("\nYONTEM 3: DIZI/ISARETCI OFFSET \n");
	for(i=0;i<=3;i++)
		printf("*(b + %d):\t%d\n",i,*(b + i));//b dizisinin adresini kullanarak erişim		
	return 0;
}
*/
/*
int main()
{
	int i=5;//i'ye 5 atadık
	int *ptr;//ptr adlı pointer tanımladık
	ptr=&i;//ptr pointer'ına i nin adresini atadık
	printf("i=%d\n",i);//i değeri
	printf("*ptr=%d\n",*ptr);//ptr pointer'ının değeri
	printf("ptr=%p\n",ptr);//ptr pointer'ının adresi(i)
	return 0;
}
*/
/*
//ÖRNEK 2
float OrtalamaBul(float dizi[],int n);//OrtalamaBul fonk.u tanımlandı
int main()
{
	float ortalama=0;
	float b[]={10,20,30,40,50};// 5 elemanlı dizi tanımlandı
	
	ortalama=OrtalamaBul(b,5);// OrtalamaBul fonk.u çağırıldı
	printf("Ortalama: %f",ortalama);
	return 0;
}
float OrtalamaBul(float dizi[],int n)
{
	int i;
	float *pdizi,toplam=0;
	pdizi=dizi;// pdizi pointer'ına dizinin başlangıç adresi atandı
	
	for(i=0;i<=n;i++)
		toplam += *(pdizi + i);// pointer ile elemanlara erişilip toplandı
	return (toplam / n);//ortalamayı döndürür
}
*/
/*
//ÖRNEK 3
void f1(int n);//f1 fonksiyonu tanımlandı
void f2(int *n);//f2 fonksiyonu tanımlandı

int main()
{
	int x=55;
	printf("x in degeri\n\n");
	printf("Fonksiyonlar cagrilmadan once	: %d\n",x);
	
	f1(x);//f1 fonksiyonu x in değeriyle çağırıldı
	printf("f1 cagirildiktan sonra		: %d\n",x);
	f2(&x);//f2 fonksiyonu x in adresiyle çağırıldı
	printf("f2 cagirildiktan sonra		: %d\n",x);
	return 0;
}
void f1(int n)
{
	n=66;//n lokal değişken olarak 66 oldu
	printf("f1 fonksiyonu icinde		: %d\n",n);
}
void f2(int *n)
{
	*n=77;//n'in bellekteki değişken olarak 77 oldu
	printf("f2 fonksiyonu icinde		: %d\n",*n);
}
*/
/*
//takas örneği
int main()
{
	int a=10,b=20,temp;
	printf("a= %d, b= %d\n",a,b);
	temp=a;//a değeri temp'e aktarıldı
	a=b;//b değeri a'ya aktarıldı
	b=temp;//temp değeri b'ye aktarıldı
	printf("a= %d, b= %d\n",a,b);
	return 0;
}
*/
/*
//ÖRNEK 4
void takas(int *x, int *y);//takas fonk.u tanımlandı
int main()
{
	int a,b;
	a=22,b=33;
	printf("takas oncesi: a= %d 	b= %d\n",a,b);//a ve b değerleri
	printf("takas oncesi: &a= %p	&b= %p\n",&a,&b);//a ve b adresleri
	takas(&a,&b);//takas fonk.u a ve b nin adresleriyle çağırıldı
	printf("\ntakas sonrasi: a= %d 	b= %d\n",a,b);//a ve b değerleri
	printf("takas sonrasi: &a= %p 	&b= %p\n",&a,&b);//a ve b adresleri
	return 0;
}
void takas(int *x, int *y)
{
	int temp;//geçici değişken tanımlandı
	temp= *x;//temp'e x pointer değeri atanır
	*x= *y;//x pointer'ına y pointer değeri atanır
	*y= temp;//y pointer'ına temp değeri atanır
}
*/
/*
int *BuyukBul(int a,int b);//BuyukBul fonk.u tanımlandı
int main()
{
	int s1,s2;
	int *p;//p pointer atandı
	
	printf("s1:");
	scanf("%d",&s1);
	printf("s2:");
	scanf("%d",&s2);
	p=BuyukBul(s1,s2);//BuyukBul fonk.u çağırıldı ve sonucu p'ye atandı
	printf("Buyuk sayi: %d",*p);
	return 0;
}
int *BuyukBul(int a,int b)
{
	return (a>b)?&a:&b;//a büyükse a, değilse b döndürür
}
*/
/*
double *maxAdr(double a[],int boyut);//maxAdr fonk.u tanımlandı
int main()
{
	double x[6]={1.1,3.3,7.1,5.4,0.2,-1.5};//6 elemanlı dizi tanımlandı
	double *p;//p pointer tanımlandı
	int k;
	for(k=0;k<6;k++)
		printf("%d %lf %p\n",k,x[k],&x[k]);//dizinin elemanları ve adreslerini sırasıyla yazdır
	p=maxAdr(x,6);//maxAdr fonk.u çağırır ve dönen adresi p'ye atar
	printf("\En buyuk deger: %f\n",*p);
	printf("En buyuk adres: %p\n",p);	
	return 0;
}
double *maxAdr(double a[],int boyut)
{
	double ebd=a[0];//en büyük değer'e dizinin ilk elemanı atandı
	double *eba=&a[0];//en büyük adres'e dizinin ilk elemanının adresi atandı
	int i;
	for(i=1;i<boyut;i++)
		if(a[i]>ebd)//mevcut eleman ebd'den büyükse
		{
			ebd=a[i];//yeni en büyük değer
			eba=&a[i];//yeni en büyük değer adresi
		}
	return eba;//en büyük değerin adresini döndürür		
}
*/
/*
void inc_ptr(int *p) {
    p=p+1; //pointer'in değeri fonk. içinde değiştiriliyor
}
int main()
{
    int A[3]={50,60,70}; //3 elemanlı bir dizi tanımlandı
    int *q=A; //q pointer'ı dizinin ilk elemanını gösteriyor
    inc_ptr(q); //Fonksiyon çağırılır ancak q'nun kendisi değişmez 
    printf("*q= %d\n",*q); //q sadece lokalde değiştiği için yine 50 verir

    return 0;
}
*/
/*
void inc_ptr(int **h)//inc_ptr fonk.u tanımlandı

{ *h = *h + 1; }//h'nin gösterdiği pointer'ı 1 ileri kaydıır

main(){

int A[3] = {50, 60, 70};//3 elemanlı bir dizi tanımlandı

int* q = A;//q dizinin ilk elemanını gösterir

printf("q icerigi= %p 	gosterdigi deger= %d\n ",q,*q);

inc_ptr(&q);//q'yu adresten değiştirdiği için q'yu değiştirebilir

printf("q icerigi= %p	 gosterdigi deger= %d\n ",q,*q);

}
*/
/*
void Hello()
{//1'den 100'e kadar olan sayıların toplamını hesaplayan fonk.
    int i, t=0;
    printf("Merhaba Dunyalilar\n");
    for (i=1;i<=100;i++)
	{
        t=t+i;
    }
    printf("toplam=%d\n", t);
}

int add(int *a, int *b)
{//iki sayının toplamını döndüren fonk.
    return *a+*b;
}

int main()
{
    int a=12,b=4;
    int toplam=add(&a,&b);//a ve b adresleriyle toplamı hesaplar
    printf("Toplam=%d\n",toplam);
    Hello();//Hello fonk.unu çağırır
    printf("Toplam=%d\n",toplam);
    return 0;
}
*/
/*
void Hello()
{//1'den 100'e kadar olan sayıların toplamını hesaplayan fonk.
    int i, t=0;
    printf("Merhaba Dunyalilar\n");
    for (i=1;i<=100;i++)
	{
        t=t+i;
    }
    printf("toplam=%d\n", t);
}

int *add(int *a, int *b)
{//iki sayının toplamını döndüren fonk.
    int *c=(int *)malloc(sizeof(int));//dinamik olarak bellek ayırır
    *c=*a+*b;
    return c;
}

int main()
{
    int a=12,b=4;
    int *p=add(&a,&b);//a ve b adresleriyle toplamı hesaplar
    printf("Toplam=%d\n",*p);
    Hello();//Hello fonk.unu çağırır
    printf("Toplam=%d\n",*p);
    return 0;
}
*/
/*
int main()
{
	int *x,i,N,toplam=0;
	float ortalama;
	printf("Eleman sayisi ");
	scanf("%d",&N);
	x=(int*)malloc(N*sizeof(int));//N kadar tam sayı için dinamik bellek ayır
	printf("Elemanlari girin:\n");
	for(i=0;i<N;i++)
	{
		printf("%d.eleman= ",i+1);
		scanf("%d",&x[i]);
		toplam+=x[i];
	}
	free(x);//dinamik belleği serbest bırakır
	ortalama=(float) toplam/N;//ortalamayı hesaplar
	printf("Bu %d sayisinin ortalamasi %f dir\n",N,ortalama);
}
*/
/*
int* buyuk(int*, int*);//buyuk fonk.y tanımlandı
int main()
{
int numa=0;
int numb=0;
int *result;//sonuç pointer'ı
printf(" birinci deger: ");
scanf("%d", &numa);
printf(" ikinci deger : ");
scanf("%d", &numb);
result=buyuk(&numa, &numb);//buyuk fonk.unu çağırıldı ve result pointer'ına atandı
printf(" buyuk olan %d \n\n",*result);
}
int* buyuk(int *n1, int *n2)
{
if(*n1 > *n2)//n1'in gösterdiği değer büyükse n1 adresi,değilse n2 adresi dödndürür
return n1;
else
return n2;
}
*/
/*
int f(int n)//
{
	int f=1,i;
	for(i=1;i<n;i++)
		f*=i;
	return f;	
}
int main()
{
	int (*pf)(int);//int tipinde pf pointer'ı tanımlandı
	pf=&f;//f fonk.nun adresi pointer'a atandı
	printf("Fonksiyonun adresi= %p\n",&f);
	printf("Fonksiyonun adresi= %p\n",pf);
	int sonuc= pf(4);//fonksiyonu çağırır
	printf("sonuc: %d\n",sonuc);
	return 0;
}
*/
/*
void yazdir(int,int,int(*)(int,int));
int kucuk(int,int);
int buyuk(int,int);

int main()
{
int a,b,secim;
printf("Iki tamsayi giriniz: ");
scanf("%d%d",&a,&b);
printf("Buyuk olani bulmak icin 1 kucuk olani bulmak icin 2 giriniz: ");
scanf("%d",&secim);
if(secim==1) yazdir(a,b,buyuk);//1 ise buyuk fonk.u cağırır
else yazdir(a,b,kucuk);//değilse kucuk fonk.u çağırır
};

void yazdir(int a,int b,int(*k)(int,int))
{
int sonuc=0;
sonuc=(*k)(a,b);//pointer k'yı kullanarak fonk.u çağırır
printf("Sonuc: %d",sonuc);
}
int kucuk(int a,int b)
{//hangisi küçükse o döner
if(a<b) return a;
else return b ;
}
int buyuk(int a,int b)
{//hangisi büyükse o döner
if(a>b) return a;
else return b ;}
*/
#include <string.h>
typedef struct
{
	char isim[50];
	int yas;
} kisi;

int main()
{
	kisi k;//k adında kisi yapısı oluşturur
	kisi *pk;//kisi yapısının pointeri
	pk=&k;//k adresini pk pointerına atar
	strcpy(k.isim,"ahmet");//ahmet ismini k'ya kopyalar
	k.yas=19;//k struct'ının yaşını 19 yapar
	pk->yas=20;//pointer ile 20 ye günceller
	printf("yas:%d\n",pk->yas);
	(*pk).yas=21;//pointer ile 21 e günceller
	printf("yas:%d\n",pk->yas);	
	return 0;
}