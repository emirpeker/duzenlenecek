#include <stdio.h>

int main()

{ float toplam=0,deger,isaret=1;

int i;

for (i=1;i<=99999;i=i+2)

{deger=isaret*(1/(float)i);

toplam=toplam+deger;

isaret=isaret*(-1);}

toplam=4.0*toplam;

printf("sonuc=%f",toplam) ;

}