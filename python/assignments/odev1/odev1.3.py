for number in range(100,1000):
    ilk=number//100
    orta=(number//10)%10
    son=number%10
    if ilk+son>orta:
        print(number,end=" ")
