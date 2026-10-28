#include <stdio.h>
#include <stdlib.h>

int main()
{
	int matrix_A[3][3];
	int i,j;
	int max,maxSatir,maxSutun,toplam;
	max=-1,maxSatir=-1,maxSutun=-1,toplam=0;
	
	printf("A matrisinin degerlerini girin(0-9):\n");
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			printf("%d. satir %d. sutun degeri: ",i,j);
			scanf("%d",&matrix_A[i][j]);
			
			if(matrix_A[i][j]<0 || matrix_A[i][j]>9)
			{
				printf("Degerler 0-9 arasinda olmalidir!");
				return 0;
			}
			if (matrix_A[i][j]>max) 
			{
                max=matrix_A[i][j];
                maxSatir=i;
                maxSutun=j;
            }
		}
	}
	printf("\nHarita:\n");
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
			printf("%4d ",matrix_A[i][j]);
			
	printf("\n\n");	
	}
	printf("\nEn buyuk sayi: %d\nKonum:[%d][%d]\n",max,maxSatir,maxSutun);	
	
	if (maxSatir>0) 
        toplam += matrix_A[maxSatir-1][maxSutun];
    
    if (maxSatir< 2) 
        toplam += matrix_A[maxSatir+1][maxSutun];
    
    if (maxSutun>0) 
        toplam += matrix_A[maxSatir][maxSutun-1];
    
    if (maxSutun<2) 
        toplam += matrix_A[maxSatir][maxSutun+1];

    printf("Komsular toplami: %d\n", toplam);

    if (toplam>15)
        printf("Hazine bulundu!\n");
    else
        printf("Hazine bulunamadi.\n");

	return 0;
}