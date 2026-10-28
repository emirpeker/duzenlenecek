#include <Stdio.h>

int main()
{
	int number1,number2,number3;
	int maxNumber,minNumber;
	printf("Please enter three number for compare: ");
	scanf("%d%d%d",&number1,&number2,&number3);
	
	if(number1>=number2 && number1>=number3)
		maxNumber = number1;
	else if (number2>number1 && number2>number3)	
		maxNumber = number2;
	else
		maxNumber = number3;
	
	if(number1<=number2 && number1<=number3)		
		minNumber = number1;
	else if(number2<number1 && number2<number3)		
		minNumber = number2;
	else		
		minNumber = number3;
	
	printf("The Largest number: %d\n",maxNumber);
	printf("The Least number: %d",minNumber);			
	return 0;
	
}