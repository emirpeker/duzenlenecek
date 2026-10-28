# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(6))

def selection_sort(arr):
    high=len(arr)-1
    lenght=len(arr)
    temp=[]
    n=0
    while n!=lenght:
        min=arr[0]
        for i in arr:
            if min>arr[i]:
                min=i
        temp[n]=min
        n+=1
    for item in temp:
        print(item)
arr=[5,2,7,6]
selection_sort(arr)        
