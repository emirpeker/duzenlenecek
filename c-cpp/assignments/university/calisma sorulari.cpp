#include <Stdio.h>
#include <Stdlib.h>
#include <time.h>

int array[10];
int i,sayi;
int max=0, min=10000;
int array_1[15];
int sayi2=0;
float ortalama=0.0;
int max2=0, min2=10000,max2_1=0;

void birinci()
{
	srand(time(NULL));
	for(i=0;i<10;i++)
	{
		sayi=rand()%100;
		array[i]=sayi;
		printf("%d. Dizi elemani= %d\n",i,array[i]);
	}
	for(i=0;i<10;i++)
	{
		if(max<array[i])
			max=array[i];
		if(min>array[i])
			min=array[i];	
	}
	printf("En buyuk sayi= %d\n",max);
	printf("En kucuk sayi= %d\n\n",min);
}

void ikinci()
{
	srand(time(NULL));
	for(i=0;i<15;i++)
	{
		sayi2=20+rand()%40;
		array_1[i]=sayi2;
		printf("%d. Dizi elemani= %d\n",i,array_1[i]);
	}
	for(i=0;i<15;i++)
	{
		if(array_1[i]>max2)
		{
			max2_1=max2;
			max2=array_1[i];
		}
		if(min2>array_1[i])
			min2=array_1[i];
				
		else if(array_1[i]>max2_1 && array_1[i]<max2)
			max2_1=array_1[i];
		
		ortalama+=array_1[i];
	}
	ortalama= ortalama/15;
	printf("En buyuk sayi= %d\n",max2);
	printf("En buyuk 2.sayi= %d\n",max2_1);
	printf("En kucuk sayi= %d\n",min2);
	printf("Dizideki sayilarin aritmetik ortalamasi= %.2f\n\n",ortalama);
}
int main()
{
	birinci();
	ikinci();
	return 0;
}