#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i;
	double wheat=1,sumWheat=0;
	
	for(i=1;i<65;i++)
	{
		printf("%d. kare icin verilecek bugday sayisi: %20.0f\n",i,wheat);
		sumWheat+=wheat;
		wheat*=2;
	}
	printf("toplam bugday sayisi: %20.0f",wheat);
	return 0;
}