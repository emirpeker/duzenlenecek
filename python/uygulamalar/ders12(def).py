# def my_name(**kwargs):
#     print("His lastname is "+kwargs["lastname"])

# my_name(fisrtname="Emir",lastname="Peker")

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# for item in range(10):
#     # print(fib(item),end=" ")

#girilen 4 basamaklı bir sayıyı function yardımıyla yazıya çeviren program

def number_to_words(number):
    ones=["","bir","iki","üç","dört","beş","alti","yedi","sekiz","dokuz"]
    tens=["","on","yirmi","otuz","kirk","elli","altmiş","yetmiş","seksen","doksan"]

    if not (1000<=number<=9999):
        return "Please enter a 4-digit number!"

    one_digit=number%10
    ten_digit=(number//10)%10
    hundred_digit=(number//100)%10
    thousand_digit=number//1000

    result=""
    if(thousand_digit>0):
        if(thousand_digit>1):
            result+=f"{ones[thousand_digit]} bin "
    else:
        result+="bin"
    
    if(hundred_digit>0):
        if(hundred_digit>1):
            result+=f"{ones[hundred_digit]} yüz "
    else:
        result+="yüz"

    if(ten_digit>0):
        result+=f"{tens[ten_digit]} "

    if(one_digit>0):
        result+=f"{ones[one_digit]} "    
    return result.strip()

number=int(input("Enter a 4-digit number:"))
print(number_to_words(number))