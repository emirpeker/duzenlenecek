#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define satir 5
#define sutun 6

void matrisOlustur(int matris[satir][sutun])
{
    for(int i=0;i<satir;i++)
	{
        for(int j=0;j<sutun;j++)
            matris[i][j]=rand()%1000+1;
    }
}

void matrisYazdir(int matris[satir][sutun])
{
    for(int i=0;i<satir;i++)
	{
        for(int j=0;j<sutun;j++)
            printf("%4d ",matris[i][j]);

        printf("\n");
    }
}
void maxs(int matris1[satir][sutun],int matris2[satir][sutun],int matris3[satir][sutun],int MaxSonuc[satir][sutun])
{
    for(int i=0;i<satir;i++)
	{
        for(int j=0;j<sutun;j++)
		{
            int max=matris1[i][j];
            if(matris2[i][j]>max)
				max=matris2[i][j];
            if(matris3[i][j]>max)
				max=matris3[i][j];
            
			MaxSonuc[i][j]=max;
        }
    }
}
void mins(int matris1[satir][sutun],int matris2[satir][sutun],int matris3[satir][sutun],int MinSonuc[satir][sutun])
{
    for(int i=0;i<satir;i++)
	{
        for(int j=0;j<sutun;j++)
		{
            int min=matris1[i][j];
            if(matris2[i][j]<min)
				min=matris2[i][j];
            if(matris3[i][j]<min)
				min=matris3[i][j];
            
			MinSonuc[i][j]=min;
        }
    }
}
void avg(int matris1[satir][sutun],int matris2[satir][sutun],int matris3[satir][sutun],int AvgSonuc[satir][sutun])
{
    for(int i=0;i<satir;i++)
	{
        for(int j=0;j<sutun;j++)
		{
            AvgSonuc[i][j]=(matris1[i][j]+matris2[i][j]+matris3[i][j])/3;
        }
    }
}

int main()
{
    int matris1[satir][sutun];
    int matris2[satir][sutun];
	int matris3[satir][sutun];
	int MaxSonuc[satir][sutun];
	int MinSonuc[satir][sutun];
	int AvgSonuc[satir][sutun];
    srand(time(0));

    matrisOlustur(matris1);
    matrisOlustur(matris2);
    matrisOlustur(matris3);
    maxs(matris1,matris2,matris3,MaxSonuc);
    mins(matris1,matris2,matris3,MinSonuc);
    avg(matris1,matris2,matris3,AvgSonuc);

    printf("Matris 1:\n");
    matrisYazdir(matris1);

    printf("Matris 2:\n");
    matrisYazdir(matris2);

    printf("\nMatris 3:\n");
    matrisYazdir(matris3);
    
    printf("\nMaxSonuc Matrisi:\n");
    matrisYazdir(MaxSonuc);
    
    printf("\nMinSonuc Matrisi:\n");
    matrisYazdir(MinSonuc);
    
    printf("\nAvgSonuc Matrisi:\n");
    matrisYazdir(AvgSonuc);

    return 0;
}
