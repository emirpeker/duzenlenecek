#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,j;
	char input,character='A';
	
	printf("Enter a uppercase letter: ");
	scanf("%c",&input);
	
	for(i=1;i<=(input-'A'+1);i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("%c",character);
		}
		character++;
		printf("\n");
	}
	
	
	return 0;	
}