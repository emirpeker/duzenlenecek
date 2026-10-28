#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
	double average=0,number[3];
	
	printf("Enter 3 numbers: ");
	scanf("%lf%lf%lf",&number[0],&number[1],&number[2]);
	
	average=(number[0]+number[1]+number[2])/3;
	printf("Average: %.3f\n",average);
	
	return 0;
}