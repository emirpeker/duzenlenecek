#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,number,j;
	
	printf("Enter a number: ");
	scanf("%d",&number);
	
	for(i=1;i<=number;i++)
	{
		for(j=1;j<=i;j++)
			printf("%d",i);
	printf("\n");
	} 
	printf("\n\n");
	for(i=0;i<=number;i++)
	{
		for(j=1;j<=number-i;j++)
			printf("%d",i+1);
	printf("\n");
	} 
	return 0;
}