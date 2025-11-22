def odd_even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
