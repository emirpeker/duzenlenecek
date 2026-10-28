#include <Stdio.h>
#include <Stdlib.h>

int main()
{
	int x,y,smallNumber;
	int obeb=0, okek=0;
	
	printf("OBEB'i ve OKEK'i bulunacak iki sayi giriniz:");
	scanf("%d%d",&x,&y);
	
	if(x<y)
		smallNumber=x;
	else
		smallNumber=y;
	for(int i=2;i<=smallNumber;i++)
	{
		if((x%i==0)&&(y%i==0))
			obeb=i;
					
	}	
	if(obeb!=0)
	{
		okek=obeb*x/obeb*y/obeb;
		printf("%d ve %d sayilarinin OBEB'i:%d\n",x,y,obeb);	
		printf("%d ve %d sayilarinin OKEK'i:%d\n",x,y,okek);	
	}
			
	else
	{
		printf("Bu sayilarin OBEB'i yoktur!");
		printf("%d ve %d sayilarinin OKEK'i:%d\n",x,y,okek);
	}
	return 0;
}