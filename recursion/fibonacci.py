print("fibonacci")

def fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

f = int(input("enter number\n"))

for i in range(0,f,1):
    print(fib(i))