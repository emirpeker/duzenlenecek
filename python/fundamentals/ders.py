def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True