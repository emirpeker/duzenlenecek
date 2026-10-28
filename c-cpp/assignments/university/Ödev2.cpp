#include <stdio.h>

int main(){
		int sayi,aralik;
    printf("1 ile 10000 arasinda bir tamsayi giriniz: ");
    scanf("%d", &sayi);

    if (sayi < 1 || sayi > 10000) {
        printf("Girdiginiz sayi 1 ile 10000 arasinda olmalidir.\n");
        return 0;
    }
     if (sayi <= 10) 
        aralik = 1; 
     else if (sayi <= 100) 
        aralik = 2; 
     else if (sayi <= 1000) 
        aralik = 3; 
     else 
        aralik = 4; 



    switch (aralik) {
        case 1:
            printf("Sayi 1-10 arasindadir.\n");
            break;
        case 2:
            printf("Sayi 11-100 arasindadir.\n");
            break;
        case 3:
            printf("Sayi 101-1000 arasindadir.\n");
            break;
        case 4:
            printf("Sayi 1001-10000 arasindadir.\n");
            break;
        default:
            printf("Bilinmeyen bir hata olustu.\n");
            break;
    }

    return 0;
}
