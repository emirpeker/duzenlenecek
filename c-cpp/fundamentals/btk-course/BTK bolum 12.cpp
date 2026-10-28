#include <Stdio.h>

int main(){
	//				DİZİLER	
		/*	int dizi[]={25,50,75,100};
			dizi[0]=33;
			
			printf("%d",dizi[2]);
		*/
			
		/*	int dizi[10]={25,50,75,100};
			int index;
			
			for(index=0;index<10;index++){
							printf("%d\n",dizi[index]);
							}	
		*/
		
		/*	int dizi[]={3,8,1,7,2,9,5,4};
			int en_buyuk_deger=dizi[0];
			int konum=0;
			
			int boyut=sizeof(dizi)/sizeof(dizi[0]);
			
			for(int index=0;index<boyut;index++){
							if(dizi[index]>en_buyuk_deger){
														en_buyuk_deger=dizi[index];
														konum=index;
															}
							}
			printf("Dizinin en buyuk elemani, %d indexli konumda bulunan %d degeridir.\n", konum,en_buyuk_deger);					
		*/
		
		/*	int eklenecek_sayi,eklenecek_index;
			int dizi[]={3,4,1,9,6,2,8};
			int boyut=sizeof(dizi)/sizeof(dizi[0]);
		
			for(int index=0;index<boyut;index++)
			printf("%d ",dizi[index]);
			
			printf("\nDiziye eklenecek sayiyi giriniz: ");
			scanf("%d",&eklenecek_sayi);
			printf("Sayinin hangi indexe eklenecegini giriniz: ");
			scanf("%d",&eklenecek_index);
			
			for(int index=boyut-1;index>eklenecek_index;index--)
			dizi[index]=dizi[index-1];
			dizi[eklenecek_index]=eklenecek_sayi;
			
			for(int index=0;index<boyut;index++)
			printf("%d ",dizi[index]);
		*/
		
//			------------------------------------		
//					ÇOK BOYUTLU DİZİLER(MATRİS)
	
	/*	int matris[2][3]={{1,4,2},{3,6,8}};
		int i,j;
		
		for(i=0;i<2;i++){
						for(j=0;j<3;j++)
						printf("%d ",matris[i][j]);
						printf("\n");
						}
	*/
	
	/*	int matris[2][3][4]={{ {3,4,2,3},{0,-3,9,11},{23,12,23,2} },
								{{13,4,56,3}, {5,9,3,5},{3,1,4,9}}};
								
		int i,j,k;
		
		for(i=0;i<2;i++){
						for(j=0;j<3;j++){
									for(k=0;k<4;k++)
									printf("%d ",matris[i][j][k]);
						printf("\n");
										}
		printf("........\n");
		}
	*/
	
			
		return 0;
	


			
			
			
			
			
			
			
			
			}