#include <stdio.h>
#include <stdlib.h>

int main(){
int a = 10, b = 6;
int *p;
int **ptr;
p=&a;
ptr = &p;
p=&b;
a=45;
printf("%d ",**ptr);
}