#include <stdio.h>
#include <stdlib.h>

void sortIt();
void writeTheArray();
void writeTheArrayReverse();	
int numbers[7];
int i;
	
int main()
{
	printf("Enter the numbers: ");
	
	for(i=0;i<7;i++)
	{
		scanf("%d",&numbers[i]);
	}	
	printf("\n Before sorting...");
	writeTheArray();
	printf("\n The array is sorting...\n");
	sortIt();
	printf("\n After sorting\n");
	writeTheArray();	
	printf("\n Reverse \t");
	writeTheArrayReverse();	
	return 0;
}

void sortIt()
{
	int reverse;
	for(i=0;i<7;i++)
	{
		for(int j=i+1;j<7;j++)
		{
			if(numbers[j]<numbers[i])
			{
				reverse=numbers[i];
				numbers[i]=numbers[j];
				numbers[j]=reverse;
			}
		}
	}
}

void writeTheArray()
{
	for(i=0;i<7;i++)
	{
		printf("\n%d ",numbers[i]);
	}
}

void writeTheArrayReverse()
{
	for(i=6;i>=0;i--)
	{
		printf("\n%d ",numbers[i]);
	}
}
