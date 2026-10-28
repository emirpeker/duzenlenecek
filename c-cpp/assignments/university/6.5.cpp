#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int sayilar[10],i;
    int toplamKarakter=0;

    srand(time(NULL));

    printf("Deger\t Toplam Karakter Sayisi\n");
	
    for(i=0;i<10;i++)
	{
        sayilar[i]=rand() %1000+1;
        int karakterSayisi=printf("%d",sayilar[i]);
        toplamKarakter+=karakterSayisi;
        printf("\t\t%d\n",toplamKarakter);
    }

    return 0;
}
