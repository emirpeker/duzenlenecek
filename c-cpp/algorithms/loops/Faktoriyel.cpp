#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,factorial,number;
	factorial=1;
	
	printf("Enter a number: ");
	scanf("%d",&number);
	
	for(i=1;i<=number;i++)
	{
		factorial*=i;
	}
	printf("%d! = %d\n",number,factorial);
	return 0;	
}