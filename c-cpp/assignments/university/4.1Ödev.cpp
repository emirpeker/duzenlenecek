#include <stdio.h>

int main() {
    int matrix_A[20][20];
    int i,j;
    int satir,sutun,maxtoplam;
    int ust,alt,sol,sag;
    
    printf("A matrisinin satir ve sutun sayisini giriniz: ");
    scanf("%d %d",&satir,&sutun);

    printf("A matrisinin degerlerini girin:\n");
    for (i=0;i<satir;i++)
	{
        for (j=0;j<sutun;j++)
		{
            printf("%d. satir %d. sutun degeri: ",i,j);
            scanf("%d",&matrix_A[i][j]);
        }
    }
    for (ust=0;ust<satir;ust++)
	{
        for (alt=0;alt<satir;alt++)
		{
            for (sol=0;sol<sutun;sol++)
			{
                for (sag=0;sag<sutun;sag++)
				{
                    int toplam = 0;
                    for (i=ust;i<=alt;i++)
					{
                        for (j=sol;j<=sag;j++)
                            toplam += matrix_A[i][j];
                    }

                    if (toplam>maxtoplam)
                    	maxtoplam = toplam;
                }
            }
        }
    }
    printf("En buyuk dikdortgen alt matris toplami: %d\n", maxtoplam);
    return 0;
}