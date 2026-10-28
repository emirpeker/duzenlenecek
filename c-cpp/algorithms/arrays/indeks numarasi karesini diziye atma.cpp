#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
	int i=0,mySquare[20];
	
	for(i=0;i<20;i++){
				mySquare[i]=i*i;
				printf("mysquare[%d]:%d\n",i,mySquare[i]);
	}
	
	return 0;
	}