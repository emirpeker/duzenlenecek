#include <Stdio.h>
#include <Stdlib.h>

int main()
{
	int	upperLimit,i,j,sum;
	
	printf("Hangi sayiya kadar olan mukemmel sayilar listelensin?\n");
	scanf("%d",&upperLimit);
	
	for(i=1;i<=upperLimit;i++)
	{
		sum=0;
		for(j=1;j<=i/2;j++)
		{
			if(i%j==0)
			sum+=j;
		}
		if(sum==i)
			printf("%d mukemmel sayidir.\n",i);
	}
	return 0;
}