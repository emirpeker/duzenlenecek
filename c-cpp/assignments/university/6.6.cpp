#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,j,sayi;
	
	printf("1-19 arasi bir sayi giriniz: ");
	scanf("%d",&sayi);
	if(sayi<1 || sayi>19 || sayi%2==0)
	{
		printf("Lutfen 1 ile 19 arasi tek bir sayi giriniz!");
		return 0;
	}
	for(i=1;i<=sayi;i+=2)
	{
        for(j=i;j<sayi;j+=2)
            printf(" ");
        for(j=1;j<=i;j++)
            printf("*");
        printf("\n");
    }

    for(i=sayi-2;i>=1;i-=2)
	{
        for(j=sayi;j>i;j-=2)
            printf(" ");
        for(j=1;j<=i;j++)
            printf("*");
        printf("\n");
    }
	return 0;
}