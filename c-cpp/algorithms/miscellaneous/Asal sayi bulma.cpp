#include <Stdio.h>
#include <Stdlib.h>

int main(){
	int i,number;
	number=0;
	i=2;
	
	printf("Enter a positive number: ");
	scanf("%d",&number);
	
	if(number<0){
		printf("Please enter a POSITIVE number!\n");
		return 0;
	}
	
	while(i<=number/2){
		if(number%i==0){
			printf("%d divided by %d so it can't be a prime number",number,i);
			return 0;		
		}
		i++;
	}
	printf("Your number is %d a prime number!",number);
	return 0;
}