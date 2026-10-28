#include <stdio.h>
#include <stdlib.h>

int main() {
			/*printf("char   									: %d bayt\n", sizeof(char));
			printf("short   								: %d bayt\n", sizeof(short));
			printf("int   									: %d bayt\n", sizeof(int));
			printf("long   									: %d bayt\n", sizeof(long));
			printf("unsigned char   						: %d bayt\n", sizeof(unsigned char));
			printf("unsigned short 							: %d bayt\n", sizeof(unsigned short));
			printf("unsigned int   							: %d bayt\n", sizeof(unsigned int));
			printf("unsigned long   						: %d bayt\n", sizeof(unsigned long));
			printf("float   								: %d bayt\n", sizeof(float));
			printf("double   								: %d bayt\n", sizeof(double));
			printf("long double   							: %d bayt\n", sizeof(long double));*/
			int a = 2 , b = 10, c = 50;
			float f = 1.05, g = 25.5, h = -0.1, yuzde;
			
			printf("3 tamsayi			: %d %d %d\n", a, b, c);
			printf("3 tamsayi	[TAB]	: %d \t%d \t%d\n", a, b, c);
			
			printf("\n");
			
			printf("3 reel sayi (yanyana)		: %f %f %f\n", f, g, h);
			printf("3 reel sayi (altalta)		: \n%f\n%f\n%f\n\n", f, g, h);

			yuzde = 220 * 25/100.0;
			
			printf("220 nin %%25 i %f dir\n", yuzde);
			printf("%f/%f isleminin sonucu = %f\n", g, f, g / f);
			
			printf("\nprogram sonunda beep sesi cikar... \a");
			
			return 0;
			
	
	
	
			}