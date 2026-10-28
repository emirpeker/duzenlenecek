#include <stdio.h>

void printBinary(unsigned int n)
{
    for(int i=7;i>=0;i--)
        printf("%d",(n >> i)&1);
    printf("\n");
}

int main()
{
    unsigned int a = 25; // 00011001
    unsigned int b = 30; // 00011110

    printf("a = %u\tBinary: ",a);
    printBinary(a);
    printf("b = %u\tBinary: ",b);
    printBinary(b);
    
    printf("\n");

    unsigned int and=a&b;
    printf("a & b = %u\tBinary: ",and);
    printBinary(and);

    unsigned int or=a|b;
    printf("a | b = %u\tBinary: ",or);
    printBinary(or);

    unsigned int xor=a^b;
    printf("a ^ b = %u\tBinary: ",xor);
    printBinary(xor);

    unsigned int not_a =~a;
    printf("~a = %u\tBinary (8 bit): ",not_a);
    printBinary(not_a & 0xFF);

    unsigned int left=a<<2;
    printf("a << 2 = %u\tBinary: ",left);
    printBinary(left);

    unsigned int right=a>>2;
    printf("a >> 2 = %u\tBinary: ",right);
    printBinary(right);

    return 0;
}
