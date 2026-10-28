#include <stdio.h>
#include <stdlib.h>

void spiralOkuma();

int row,column;
int i,j,k;
int matrix_A[20][20];

int main()
{
	printf("A matrisinin satir ve sutun sayisini giriniz: ");
	scanf("%d%d",&row,&column);
	printf("A matrisinin degerlerini girin:\n");
	
	for(i=0;i<row;i++)
	{
		for(j=0;j<column;j++)
		{
			printf("%d. satir %d. sutun degeri: ",i,j);
			scanf("%d",&matrix_A[i][j]);
		}
	}
	spiralOkuma();
	return 0;
}

void spiralOkuma()
{
	int ust=0,alt=row-1;
	int sol=0,sag=column-1;
	
	while(ust<=alt && sol<=sag)
	{
		for(i=sol;i<=sag;i++)
			printf("%d ",matrix_A[ust][i]);
		ust++;
		
		for(i=ust;i<=alt;i++)	
			printf("%d ",matrix_A[i][sag]);
		sag--;
		
		if(ust<=alt)
		{
			for(i=sag;i>=sol;i--)
				printf("%d ",matrix_A[alt][i]);
			alt--;	
		}
		
		if(sol<=sag)
		{
			for(i=alt;i>=ust;i--)
				printf("%d ",matrix_A[i][sol]);
			sol++;	
		}
	}
	printf("\n");
}

