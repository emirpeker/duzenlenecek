#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void matrisOlustur(int row,int col,int matris[row][col])
{
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
            matris[i][j]=(rand()%71)+5;
    }
}

void matrisYazdir(int row,int col,int matris[row][col])
{
    printf("\nMatris:\n");
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
            printf("%3d ",matris[i][j]);
        printf("\n");
    }
}

void dosyaYazBinary(int row,int col,int matris[row][col],const char* dosya)
{
    FILE* d=fopen(dosya,"wb");
    if(d==NULL)
    {
        printf("Dosya acilamadi..\n");
        return;
    }
    for(int i=0;i<row;i++)
    {
        int max=0,secondMax=0;
        int index1=0,index2=0;
        for(int j=0;j<col;j++)
        {
            if(matris[i][j]>max)
            {
                secondMax=max;
                index2=index1;
                max=matris[i][j];
                index1=j;
            } 
            else if(matris[i][j]>secondMax && matris[i][j]!=max)
            {
                secondMax=matris[i][j];
                index2=j;
            }
        }
        int veri[5]={i,max,index1,secondMax,index2};
        fwrite(veri,sizeof(int),5,d);
        printf("[%d. Satir] Max: %d (indis: %d), 2. Max: %d (indis: %d)\n",i,max,index1,secondMax,index2);
    }
    fclose(d);
    printf("\nBilgiler '%s' dosyasina kaydedildi!\n",dosya);
}

void satirSirala(int satirNo,int row,int col,int matris[row][col])
{
    if(satirNo<0 || satirNo>=row)
    {
        printf("Hatali satir numarasi!\n");
        return;
    }
    for(int i=0;i<col-1;i++)
    {
        for(int j=i+1;j<col;j++)
        {
            if(matris[satirNo][i]<matris[satirNo][j])
            {
                int tmp=matris[satirNo][i];
                matris[satirNo][i]=matris[satirNo][j];
                matris[satirNo][j]=tmp;
            }
        }
    }
}

void satirSiraliDosyayaYaz(int satirNo,int row,int col,int matris[row][col],const char* dosyaAdi)
{
    if(satirNo<0 || satirNo>=row)
    {
        printf("Hatali satir numarasi!\n");
        return;
    }
    FILE* f=fopen(dosyaAdi,"w");
    if(f==NULL)
    {
        printf("Dosya acilamadi\n");
        return;
    }
    for(int i=0;i<col;i++)
        fprintf(f, "%d ",matris[satirNo][i]);
    fclose(f);
    printf("\nSatir '%d' sirali olarak '%s' dosyasina yazildi.\n",satirNo,dosyaAdi);
}

void satirGoruntule(int satirNo,int row,int col,int matris[row][col])
{
    if(satirNo<0 || satirNo>=row)
    {
        printf("Hatali satir numarasi!\n");
        return;
    }
    printf("\nSatir %d: ",satirNo);
    for(int i=0;i<col;i++)
        printf("%d ",matris[satirNo][i]);
    printf("\n");
}

int main()
{
    srand(time(NULL));
    int row=0,col=0;
    int matris[100][100];
    int secim,satirNo;

    do{
        printf("\n--- MENU ---\n");
        printf("1. Matris Olustur ve Binary Dosyaya Yaz\n");
        printf("2. Satir Sirala\n");
        printf("3. Satir Goruntule\n");
        printf("4. Sirali Satiri Sirali Erisimli Dosyaya Yaz\n");
        printf("0. Cikis\nSeciminiz: ");
        scanf("%d",&secim);

        switch(secim){
            case 1:
                printf("Matris boyutunu gir (satir sutun): ");
                scanf("%d %d",&row,&col);
                matrisOlustur(row,col,matris);
                matrisYazdir(row,col,matris);
                dosyaYazBinary(row,col,matris,"veri.dat");
                break;

            case 2:
                if(row==0 || col==0)
                {
                    printf("Lutfen once matris olusturun!\n");
                    break;
                }
                printf("Siralanacak satir numarasini girin: ");
                scanf("%d",&satirNo);
                satirSirala(satirNo,row,col,matris);
                printf("Siralanmis hali: ");
                satirGoruntule(satirNo,row,col,matris);
                break;

            case 3:
                if(row==0 || col==0)
                {
                    printf("Lutfen once matris olusturun!\n");
                    break;
                }
                printf("Goruntulenecek satir numarasini girin: ");
                scanf("%d",&satirNo);
                satirGoruntule(satirNo,row,col,matris);
                break;

            case 4:
                if(row==0 || col==0)
                {
                    printf("Lutfen once matris olusturun!\n");
                    break;
                }
                printf("Sirali yazilacak satir numarasini girin: ");
                scanf("%d",&satirNo);
                satirSiraliDosyayaYaz(satirNo,row,col,matris,"sirali.txt");
                break;

            case 0:
                printf("Cikis yapiliyor...\n");
                break;

            default:
                printf("Gecersiz secim!\n");
        }
    } while(secim!=0);

    return 0;
}
