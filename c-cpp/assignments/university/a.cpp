#include <stdio.h>

#include <stdlib.h>

#include <time.h>

int main()

{

int a;

srand(time(NULL));

a=rand();

printf("%d",a);

}