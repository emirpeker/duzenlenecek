#include <Stdio.h>
#include <stdlib.h>

#define VERI_BOYUTU 1000

int main(){
/*	char veri[VERI_BOYUTU];
	
	FILE*fPtr;//FİLE PoiNTER TO HOLD REFERENCE TO OUR FİLE
	//DOSYAYI w(WRİTE) MODUNDA AÇ.
	fPtr= fopen("Deneme_Metni.txt","w+");
	if(fPtr==NULL){
		//DOSYA OLUŞTURULAMADIĞI İÇİN PROGRAMDAN ÇIK
		printf("Dosya olusturulamadi.\n");
		exit(EXIT_FAILURE);
	}
//DOSYAYA KAYDEDİLECEK OLAN GİRDİLERİ KULLANICIDAN AL	
	printf("Dosyaya kaydedilecek olan girdiyi al: \n");
	fgets(veri,VERI_BOYUTU,stdin);
	
	fputs(veri,fPtr);//VERİYİ DOSYAYA YAZ
	fclose(fPtr);//DOSYAYI KAPAT
	
	printf("Dosya basariyla olusturuldu ve icerigi kaydedildi.. \n");
	
*/

/*	FILE*fPtr;//
	
	char karakter;//
	//OKUMAK İÇİN AÇ
	fPtr=fopen("Deneme_Metni.txt","r");
	if(fPtr==NULL){
		//DOSYA OLUŞTURULAMADIĞI İÇİN PROGRAMDAN ÇIK
		printf("Dosya okunamadi.\n");
		printf("Dosyanin ilgili konumda olup olmadigini ve de erisim yetkiniz olup olmadigini kontrol ediniz. \n");
		exit(EXIT_FAILURE);
				}
		printf("Dosya basariyla acildi; icerigi okunuyor.\n\n");		
		
		do{
			karakter=fgetc(fPtr);//DOSYADAN KARAKTER OKU
			putchar(karakter);//OKUDUGUN KARAKTERİ KONSOLA YAZDIR
		}		
		while(karakter != EOF);//BUNU END OF FİLE KARAKTERİNE DENK GELMEDİĞİN SURECE YAP
		fclose(fPtr);//DOSYAYLA İŞ BİTTİ.

*/

/*		int bolunen=20,bolen=0,bolum;
		
		if(bolen==0){
			fprintf(stderr,"Sifira bolme hatasi! Programdan cikiliyor..\n");
			exit(-1);//exit(EXIT_FAILURE);
		}
		
		bolum=bolunen/bolen;
		fprintf(stderr,"Bolum(Sonuc): %d\n",bolum);
		
		exit(0);
		
*/

		
		return 0;
}