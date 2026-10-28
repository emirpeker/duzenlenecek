#include <Stdio.h>
#include <math.h>

/*		float cembercapihesapla(float yaricap);
		float cembercevresihesapla(float yaricap);
		float dairealanihesapla(float yaricap);
int main(){
			float yaricap,cap,cevre,alan;
			
			printf("Cemberin/Dairenin yaricapini giriniz: ");
			scanf("%f",&yaricap);
			
			cap=cembercapihesapla(yaricap);
			cevre=cembercevresihesapla(yaricap);
			alan=dairealanihesapla(yaricap);
			
			printf("Cemberin capi= %.2f birimdir.\n",cap);
			printf("Cemberin cevresi= %.2f birimdir.\n",cevre);
			printf("Dairenin alani= %.2f birim karedir.",alan);
			return 0;
}

float cembercapihesapla(float yaricap){
									return(2*yaricap);
										}
										
float cembercevresihesapla(float yaricap){
									return(2 * M_PI * yaricap);
										}
										
float dairealanihesapla(float yaricap){
									return(M_PI * yaricap * yaricap);
										}	
	*/									
// -------------------------------------------

/*int sayiciftMi(int sayi)
{
	if((sayi%2)==0)
	return 1;
	else
	return 0;
										}										
int main()
{
	int sayi;
	
	printf("Sayiyi giriniz: ");
	scanf("%d",&sayi);
	
	if(sayiciftMi(sayi))
	printf("Sayi cifttir.");
	else
	printf("Sayi tektir");
	return 0;
										}										
*/
//----------------------------------------------

/*int sayininkubuhesapla(int sayi);

int main()
{
	int sayi,c;
	
	printf("Sayi giriniz: ");
	scanf("%d",&sayi);
	
	c=sayininkubuhesapla(sayi);
	
	printf("%d sayisinin kubu= %d",sayi,c);
	return 0;
	
										}										
int sayininkubuhesapla(int sayi)
{
	return(sayi*sayi*sayi);
										}										
*/
//-------------------------------------------------

/*int sayiasalMi(int sayi);

int main()
{
	int sayi;
	
	printf("Bir sayi giriniz: ");
	scanf("%d",&sayi);
	
	if(sayiasalMi(sayi))
	printf("%d asaldir.\n",sayi);
	else
	printf("%d asal degildir.\n",sayi);
	
	return 0;
										}										

int sayiasalMi(int sayi)
{
	int i;
	for(i=2;i<=sayi/2;i++){
					if(sayi%i==0)
					return 0;
						}
	return 1;					
										}										
*/										
//------------------------------------------

/*int sayiArmstrongMu(int sayi);

int main()										
{
	int sayi;
	
	printf("Sayi giriniz: ");
	scanf("%d",&sayi);
	
	if(sayiArmstrongMu(sayi))
	printf("%d Armstrong sayidir.\n",sayi);
	else
	printf("%d Armstrong degildir.\n",sayi);
	return 0;
										}										
int sayiArmstrongMu(int sayi)
{
	int son_basamak,toplam,orji_sayi,basamak_sayi;
	toplam=0;
	orji_sayi=sayi;
	
	basamak_sayi=(int)log10(sayi)+1;
	
	while(sayi>0){
	son_basamak=sayi%10;
	toplam=toplam+round(pow(son_basamak,basamak_sayi));
	sayi=sayi/10;
					}					
	return(orji_sayi==toplam);				
					}										
*/
//---------------------------------------------
/*int sayimukemmelMi(int sayi);

int main()
{
	int sayi;
	
	printf("Sayi giriniz: ");
	scanf("%d",&sayi);
	
	if(sayimukemmelMi(sayi))
	printf("%d mukemmeldir.\n",sayi);
	else
	printf("%d mukemmel degildir.\n",sayi);
	return 0;
}
										
int sayimukemmelMi(int sayi){
	int i,toplam,n;
	toplam=0;
	n=sayi;
	
	for(i=1;i<n;i++){
		if(n%i==0)
		toplam+=i;
	}
	return(sayi==toplam);
}										
*/	
//------------------------------------
//------------------------------------									
/*int sayimukemmelMi(int sayi);
int sayiArmstrongMu(int sayi);
int sayiasalMi(int sayi);
int main()
{
	int sayi;
	
	printf("Sayi giriniz: ");
	scanf("%d",&sayi);	
	
	if(sayiasalMi(sayi))
	printf("%d asaldir.\n",sayi);
	else
	printf("%d asal degildir.\n",sayi);
	
	if(sayiArmstrongMu(sayi))
	printf("%d Armstrong sayidir.\n",sayi);
	else
	printf("%d Armstrong degildir.\n",sayi);
	
	if(sayimukemmelMi(sayi))
	printf("%d mukemmeldir.\n",sayi);
	else
	printf("%d mukemmel degildir.\n",sayi);	
	
	return 0;								
}

int sayiasalMi(int sayi)
{
	int i;
	for(i=2;i<=sayi/2;i++){
					if(sayi%i==0)
					return 0;
						}
	return 1;					
										}
										
										
int sayiArmstrongMu(int sayi)
{
	int son_basamak,toplam,orji_sayi,basamak_sayi;
	toplam=0;
	orji_sayi=sayi;
	
	basamak_sayi=(int)log10(sayi)+1;
	
	while(sayi>0){
	son_basamak=sayi%10;
	toplam=toplam+round(pow(son_basamak,basamak_sayi));
	sayi=sayi/10;
					}					
	return(orji_sayi==toplam);				
					}		
					
															
int sayimukemmelMi(int sayi){
	int i,toplam,n;
	toplam=0;
	n=sayi;
	
	for(i=1;i<n;i++){
		if(n%i==0)
		toplam+=i;
	}
	return(sayi==toplam);
}														
*/
//--------------------------------------
//--------------------------------------
int faktoryelhesapla(int n);
int nincifibonaccihesapla(int x);
int main(){
	int deger=7;
	int x1=0,x2=1;
	printf("%d!=%d\n",deger,faktoryelhesapla(deger));
	printf("Fibonacci dizisinden ilk kac elemaninin hesaplanmasini istersiniz?: ");
	int adet;
	scanf("%d",&adet);
	int x3,i;
	
	printf("%d %d ",x1,x2);
	
	for(i=2;i<adet;i++){
		x3=x1+x2; printf("%d ",x3);
		x1=x2;
		x2=x3;
	}	
	return 0;
	
}
int faktoryelhesapla(int n){
	int f;
	if(n==1)
	f=1;
	else
	f=n*faktoryelhesapla(n-1);
	
	return(f);
	
}
int nincifibonaccihesapla(int x){
	if(x==1)
	return 0;
	else if(x==2)
	return 1;
	else 
	return nincifibonaccihesapla(x-1)+nincifibonaccihesapla(x-2);
}										
										
										
										
										
										
										
										
										
																													