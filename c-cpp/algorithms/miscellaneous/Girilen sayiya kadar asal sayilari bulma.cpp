#include <Stdio.h>
#include <Stdlib.h>

int main(){
	int i,number,j,control;
	
	printf("Enter a positive number: ");
	scanf("%d",&number);
	
	for(i=2;i<=number;i++){
		control=2;
			for(j=2;j<=i/2;j++){
					if(i%j==0){
						control=0;
						break;
					}
			}
		if(control!=0){
			printf("%d\n",i);
		}	
	}
	return 0;
}