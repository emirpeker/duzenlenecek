#include <stdio.h>
#include <stdlib.h>

int main() 
{
	int size;
	int i,j;
	
	printf("Enter size of square matrix(1-10): ");
	scanf("%d",&size);
	
	int matrix[size][size];
	
	for(i=0;i<size;i++)
	{
		for(j=0;j<size;j++)
		{
			matrix[i][j]=0;	
		}
	}
	for(i=0;i<size;i++)
	{
			matrix[i][i]=1;//major
			matrix[i][size-1-i]=1;//minör
	}
	for(i=0;i<size;i++)
	{
		for(j=0;j<size;j++)
		{
			printf("%4d",matrix[i][j]);
		}
		printf("\n\n");
	}
	return 0;
}