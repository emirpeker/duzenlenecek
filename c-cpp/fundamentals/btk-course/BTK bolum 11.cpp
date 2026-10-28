#include <Stdio.h>

int main(){
	//			FOR DÖNGÜ
	/*int i, n;
	
	printf("Ust sinir degerini giriniz: ");
	scanf("%d", &n);
	
	printf("1'den %d'ye kadar tum sayma sayilari: \n", n);		
	
	for(i=n; i>=1;i--) {
					printf("%d\n", i);
						
					    }
	*/
	
	//			FOR TOPLAMA	
	/*int i, n, toplam=0;
	
	printf("Ust sinir degerini giriniz: ");
	scanf("%d", &n);		
	
	for(i=1; i<=n;i++) {
						toplam += i;
					    }
	printf("Ilk %d adet dogal sayinin toplami= %d", n, toplam);
	*/
	
	/*int i, alt_sinir, ust_sinir, toplam=0;
	printf("Alt sinir degerini giriniz: ");
	scanf("%d", &alt_sinir);
	printf("Ust sinir degerini giriniz: ");
	scanf("%d", &ust_sinir);
	
	for(i=alt_sinir;i<=ust_sinir;i++){
					toplam+=i;
	}
	printf("%d ve %d arasindaki dogal sayilarin toplami: %d",alt_sinir, ust_sinir, toplam);
	*/
	
	/*int i,n;
	printf("Ust sinir degerini giriniz: ");
	scanf("%d", &n);
	printf("1'den %d'ye kadar tum cift sayilar: \n",n);	
	
	for(i=1;i<=n;i++){
				if(i%2==0){
						printf("%d\n",i);
				}
	}
	*/
	
	/*int i,sayi;
	printf("Carpanlari hesaplanacak sayiyi giriniz: ");
	scanf("%d", &sayi);
	printf("%d sayisinin tum carpanlari: \n",sayi);
	for(i=1;i<=sayi;i++){
				if(sayi%i==0){
						printf("%d, ", i);
							}
	}
	*/
	
	/*int i, sayi;
	printf("Carpim tablosu olusturulacak olan sayiyi giriniz: ");
	scanf("%d",&sayi);
	
	for(i=1;i<=10;i++){
				printf("%d * %d = %d\n", sayi, i,(sayi*i));
		}
*/

/*	int i=0;
	
	for(i=1;i<=10;i++){
						if(i==4){
								break;
							}
			printf("%d\n",i);
			}
*/
	/*int i;
	
	for(i=0;i<10;i++){
					if(i==5){
								continue;
							}
		printf("%d\n",i);
		}
	*/
	
/*	int i,n;
	printf("Ust sinir degerini giriniz: ");
	scanf("%d",&n);
	printf("1'den %d'ye kadar tum sayma sayilari: \n",n);
	
	for(i=1;i<=n;i++)
		printf("%d\n",i);	
	printf("...\n");
	
	i=1;
	while(i<=n){
				printf("%d\n",i);
				i++;
				}
	printf("...\n");
	
	i=1;
	do{
		printf("%d\n",i);
				i++;
		}
		while(i<=n);			
	*/
	
	/*int i;
	i=0;
	while(i<10){
				if(i==5)
				break;
				
				printf("%d\n",i);
				i++;
				}
	*/
	
	int i=0;
	while(i<10){
				if(i==4){
					continue;
						}
				printf("%d\n",i);
				i++;
				}		
	
	return 0;				    
	
	
	
	
	
	
	
	
	
}