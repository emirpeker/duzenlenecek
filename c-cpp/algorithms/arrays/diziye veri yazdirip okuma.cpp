#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
	double myValue,myArray[10];
	int choice,index;
	
	do{
		printf("Make a choice (-1 to Exit)\n");
		printf("\t1. Write,to array\n");
		printf("\t2. Read from array\n");
		printf("\t3. Read all values\n");
		scanf("%d",&choice);
		if(choice==-1) break;
		if(choice!=1 && choice!=2 && choice !=3) {
		printf("R U KIDDING ME?\n"); continue;
		}
		
		if(choice!=3){
			printf("Enter array index: ");
			scanf("%d",&index);
		}
		if(index<0 || index>9){
			printf("index should be in the range of 0-9\n");
			continue;
		}
		switch(choice){
			case 1:
					printf("\nEnter the value: ");
					scanf("%lf",&myValue);
					myArray[index]=myValue;
					printf("The write operation is successful\n\n");
					break;
			case 2:
					printf("myArray[%d]: %.2f\n\n",index,myArray[index]);
					break;		
			case 3:
					for(int m=0;m<=10;m++){
					
					printf("myArray[%d]: %.2f\n\n",m,myArray[m]);
					}
					break;		
		}
	}
	while(choice!=-1);

	return 0;
}