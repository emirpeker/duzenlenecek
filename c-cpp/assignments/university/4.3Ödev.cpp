#include <stdio.h>
#include <stdlib.h>

void sumRC();

int sum,rsum,csum,maxSum;
int i,j;
int matrix_A[4][4];

int main()
{
	printf("A matrisinin degerlerini girin:\n");
	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			printf("%d. satir %d. sutun degeri: ",i,j);
			scanf("%d",&matrix_A[i][j]);
		}
	}
	printf("\n");
	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			printf("%4d ",matrix_A[i][j]);
			
	printf("\n\n");	
	}			
	printf("\n");
	
	for(i=0;i<4;i++)
	{
	printf("\n%d. satir toplami: ",i);
	
		for(j=0;j<4;j++)
			sum+=matrix_A[i][j];
			
	printf("%d ",sum);
	sum=0;
	}
	printf("\n\n");	
	
	for(j=0;j<4;j++)
	{
	printf("%d. sutun toplami: ",j);
	
		for(i=0;i<4;i++) 
			sum+=matrix_A[i][j];
		
	printf("%d \n",sum);	
	sum=0;	
	}
	sumRC();
	
	return 0;
}

void sumRC()
{
	rsum=0,csum=0,maxSum=0;
	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			rsum += matrix_A[i][j];
	if(rsum>maxSum)
		maxSum=rsum;	
	rsum=0;	
	}
	
	for(j=0;j<4;j++)
	{
		for(i=0;i<4;i++)
			csum += matrix_A[i][j];
	if(csum>maxSum)
		maxSum=csum;
	csum=0;
	}
	printf("\nEn buyuk toplam: %d",maxSum);
}

