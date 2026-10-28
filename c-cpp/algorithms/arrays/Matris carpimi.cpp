#include <stdio.h>
#include <stdlib.h>

int main()
{
	int i,j,k,sum=0;
	int x[50][50],y[50][50],result[50][50];
	int xrows,xcolumns,yrows,ycolumns;
	
	printf("X matrisinin satir ve sutun sayisini gir: ");
	scanf("%d%d",&xrows,&xcolumns);
	printf("X matrisinin degerlerini girin:\n");
	
	for(i=0;i<xrows;i++)
	{
		for(j=0;j<xcolumns;j++)
		{
			printf("%d. satir %d. sutun degeri: ",i,j);
			scanf("%d",&x[i][j]);
		}
	}
	
	printf("Y matrisinin satir ve sutun sayisini gir: ");
	scanf("%d%d",&yrows,&ycolumns);
	
	if(xrows!=ycolumns) printf("Bu matrisler CARPILAMAZ!");
	
	else 
	{
	printf("Y matrisinin degerlerini girin:\n");
	
	for(i=0;i<yrows;i++)
	{
		for(j=0;j<ycolumns;j++)
		{
			printf("%d. satir %d. sutun degeri: ",i,j);
			scanf("%d",&y[i][j]);
		}
	}
	}
	for(i=0;i<xrows;i++)
	{
		for(j=0;j<ycolumns;j++)
		{
			
			for(k=0;k<yrows;k++)
			{
				sum+=x[i][k]*y[k][j];
			}
		result[i][j]=sum;
		sum=0;	
		}
	}
	printf("Sonuc:\n");
	for(i=0;i<xrows;i++)
	{
		for(j=0;j<ycolumns;j++)
		{
			printf("%5d",result[i][j]);
		}
		printf("\n\n");
	}
	printf("\n");
	return 0;
}