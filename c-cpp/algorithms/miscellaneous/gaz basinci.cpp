#include <Stdio.h>
#include <Stdlib.h>
#define constantR 0.082

int main()
{
	float pressure;
	int numberofmoles,volume,heat;
	printf("Please enter the VOLUME of the contanier: ");
	scanf("%d",&volume);
	printf("Please enter the NUMBER OF MOLES in the contanier: ");
	scanf("%d",&numberofmoles);
	printf("Please enter the HEAT: ");
	scanf("%d",&heat);
	
	pressure = (numberofmoles * constantR * heat)/volume;
	
	printf("PRESSURE of the contanier is= %f",pressure);
	return 0;
}