#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct
{
    int ogrNo;
    int cevaplar[20];
}Ogrenci;

int main()
{
    Ogrenci ogr[10];
    int cevapAnahtari[20];
    int sonuc[10][3];

    FILE* d;
    srand(time(NULL));

    printf("Cevap Anahtari: \n");
    for(int i=0;i<20;i++)
    {
        cevapAnahtari[i]=rand()%4+1;
        printf("%d ",cevapAnahtari[i]);
    }
    printf("\n\n");

    for(int i=0;i<10;i++)
    {
        ogr[i].ogrNo=1000+i;
        for(int j=0;j<20;j++)
        {
            int secim=rand()%5;
            ogr[i].cevaplar[j]=secim;
        }
    }

    for(int i=0;i<10;i++)
    {
        int dogru=0, yanlis=0, bos=0;
        for(int j=0;j<20;j++)
        {
            int cevap=ogr[i].cevaplar[j];
            if(cevap==0)
                bos++;
            else if(cevap==cevapAnahtari[j])
                dogru++;
            else
                yanlis++;        
        }
        sonuc[i][0]=dogru;
        sonuc[i][1]=yanlis;
        sonuc[i][2]=bos;
    }

    d=fopen("sonuclar.txt","w");
    if(d==NULL)
    {
        printf("Dosya acilamadi...");
        return 1;
    }
    fprintf(d,"OgrenciNo\tDogru\tYanlis\t\tBos\n");
    for(int i=0;i<10;i++)
    {
        fprintf(d,"%d\t\t\t%d\t\t%d\t\t%d\n",ogr[i].ogrNo,sonuc[i][0],sonuc[i][1],sonuc[i][2]);
    }
    fclose(d);
    printf("Sonuclar basariyla kaydedildi!");
    return 0;
}