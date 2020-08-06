print("fibonacci")

def fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

f = int(input("enter number till which you want series\n"))

for i in range(f):
    if(fib(i) <= f):
        print(fib(i))    
    else:
        break