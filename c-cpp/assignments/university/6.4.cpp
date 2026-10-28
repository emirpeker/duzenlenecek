#include <stdio.h>

int main()
{
    int noktaSayi,i,j;
    
	printf("Kac tane nokta gireceksiniz? : ");
    scanf("%d", &noktaSayi);

	double noktalar[noktaSayi][2];
    for(i=0;i<noktaSayi;i++)
	{
        printf("%d. nokta icin x ve y degerlerini girin:",i+1);
        scanf("%lf%lf",&noktalar[i][0],&noktalar[i][1]);
    }

    for(i=0;i<noktaSayi-1;i++)
	{
        for(j=0;j<noktaSayi-i-1;j++)
		{
            double uzaklik1=noktalar[j][0] * noktalar[j][0] + noktalar[j][1] * noktalar[j][1];
            double uzaklik2=noktalar[j+1][0] * noktalar[j+1][0] + noktalar[j+1][1] * noktalar[j+1][1];
            if(uzaklik1>uzaklik2|| (uzaklik1==uzaklik2 && noktalar[j][0]>noktalar[j+1][0]) || (uzaklik1==uzaklik2 && noktalar[j][0]==noktalar[j+1][0] && noktalar[j][1]>noktalar[j+1][1]))
			{
                double x=noktalar[j][0];
                double y=noktalar[j][1];
                noktalar[j][0]=noktalar[j+1][0];
                noktalar[j][1]=noktalar[j+1][1];
                noktalar[j+1][0]=x;
                noktalar[j+1][1]=y;
            }
        }
    }

    printf("\nSiralanmis noktalar (x, y):\n");
    for(i=0;i<noktaSayi;i++)
        printf("(%.2f, %.2f)\n",noktalar[i][0],noktalar[i][1]);

    return 0;
}
