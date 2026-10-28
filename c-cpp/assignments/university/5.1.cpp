#include <stdio.h>
#include <stdlib.h>

void reverse();

int i,e;
int array[9999];

int main()
{
	printf("Lutfen dizinin eleman sayisini giriniz: ");
	scanf("%d",&e);
	
	printf("Orijinal dizi: ");
	for(i=0;i<e;i++)
		scanf("%d", &array[i]);
	
	printf("Ters cevrilmis dizi: ");
	reverse();
	return 0;
}

void reverse()
{
	for(i=e-1;i>=0;i--)
		printf("%d ",array[i]); }
