#include <Stdio.h>
#include <Stdlib.h>

int main()
{
	int sayi;
	printf("Please enter a 4 digit number: ");
	scanf("%d",&sayi); 
	if (sayi<1000 || sayi>9999)
		{
		printf("You didnt enter a 4 digit number..!");
		return 0;
		}
	else
	{
	int udigit = sayi%10;
	int tedigit = (sayi/10)%10;
	int hdigit = (sayi/100)%10;
	int tdigit = sayi/1000;
	int sum = tdigit + hdigit + tedigit + udigit;
	printf("Sum of the 4 digit= %d",sum);
	}
	
	return 0;
}