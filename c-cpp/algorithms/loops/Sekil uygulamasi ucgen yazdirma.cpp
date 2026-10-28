#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,j,sharp=0;
	
	printf("Enter the number of sharps: ");
	scanf("%d",&sharp);
	
	for(i=1;i<=sharp;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("#");
		}
	printf("\n");	
	}
	printf("\n\n");	
	
	for(i=sharp;i>=1;i--)
	{
		for(j=1;j<=i;j++)
		{
			printf("#");
		}
	printf("\n");	
	}
	
	return 0;
}