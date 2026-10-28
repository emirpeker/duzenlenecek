#include <Stdio.h>

int main()
{
	int specialNumber,number;
	
	printf("Please enter a 4 digit number: ");
	scanf("%d",&number);
	if(number<1000 && number>9999){
		printf("You didnt enter a 4 digit number!!!");
		return 0;
	}
	
	int udigit = number%10;
	int tedigit = (number/10)%10;
	int hdigit = (number/100)%10;
	int tdigit = number/1000;
	specialNumber = ((tdigit*hdigit) + (tedigit*udigit)) * ((tdigit*hdigit) + (tedigit*udigit));
	
	if(specialNumber==number)
		printf("You entered a 'special' number. CONGRULATIONS...");
	else
		printf("You entered a normal number.");	
	return 0;
}