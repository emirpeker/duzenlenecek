#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*int myArray[5];
int i;

void tersYazdir(int myArray[5], int i);

int main()
{
	int dizi[5];
	printf("Orijinal dizi: ");
	for(i=0;i<5;i++)
	{
		dizi[i]=rand()%100+1;
		printf(" %d ",dizi[i]);
	}
	printf("\n");
	int uzunluk = sizeof(dizi) / sizeof(dizi[0]);
    tersYazdir(dizi, uzunluk);
    return 0;		
}

void tersYazdir(int myArray[5],int i)
{
	if(i==0) 
		return;
	printf("%d ",myArray[i-1]);
	tersYazdir(myArray,i-1);	
}
*/

/*int main() {
    int dizi[10];
    int i, max = -1;

    srand(time(NULL));

    printf("Orijinal dizi: ");
    for (i = 0; i < 10; i++) {
        dizi[i] = rand() % 100 + 1;
        printf("%d ", dizi[i]);
    }

    printf("\n");

    for (i = 0; i < 10; i++) {
        if (dizi[i] > max)
            max = dizi[i];
    }

    printf("Maksimum deger: %d\n", max);

    return 0;
}
*/

void degerArtir(int x) {
    x = x + 10;
    printf("Fonksiyon icinde x: %d\n", x);
}

void referansArtir(int *x) {
    *x = *x + 10;
    printf("Fonksiyon icinde x: %d\n", *x);
}

int main() {
    int num = 5;
    printf("Fonksiyondan once num: %d\n", num);
    degerArtir(num);
    printf("Fonksiyondan sonra num: %d\n", num);
    
    int nums = 5;
    printf("Fonksiyondan once num: %d\n", nums);
    referansArtir(&nums);
    printf("Fonksiyondan sonra num: %d\n", nums);
    return 0;
}



