#include <stdio.h>
#include <stdlib.h>

int main(){
/*	int n,i, *isaretci,toplam=0;

	printf("Toplanacak eleman sayisini giriniz: ");
	scanf("%d", &n);

	isaretci =(int*) malloc(n*sizeof(int));

	if(isaretci==NULL){
		printf("Hata! Bellek ayirma islemi basarisiz oldu.");
		exit(0);
	}

	printf("Toplanacak elemanlari giriniz: ");
	for(i=0;i<n;i++){
		scanf("%d", isaretci+i);
		toplam += *(isaretci+i);
	}

	printf("Toplam = %d", toplam);

	free(isaretci);
*/

/*	int n,i, *isaretci,toplam=0;

	printf("Toplanacak eleman sayisini giriniz: ");
	scanf("%d", &n);

	isaretci =(int*) calloc(n,sizeof(int));

	if(isaretci==NULL){
		printf("Hata! Bellek ayirma islemi basarisiz oldu.");
		exit(0);
	}

	printf("Toplanacak elemanlari giriniz: ");
	for(i=0;i<n;i++){
		scanf("%d", isaretci+i);
		toplam += *(isaretci+i);
	}

	printf("Toplam = %d", toplam);

	free(isaretci);
*/

/*	int *isaretci,i,n1,n2;
	printf("Boyut Giriniz: ");
	scanf("%d",&n1);

	isaretci =(int*) malloc(n1*sizeof(int));

	printf("Ayrilan ilk bellek adresleri:\n");
	for(i=0;i<n1;i++)
	printf("%pc\n",isaretci+i);

	printf("\nYeni boyut giriniz: ");
	scanf("%d",&n2);

	isaretci = realloc(isaretci, n2 * sizeof(int));

	printf("Ayrilan yeni bellek adresleri:\n");
	for(i=0;i<n2;++i)
	printf("%pc\n",isaretci+i);

	free(isaretci);
*/


    return 0;
}
