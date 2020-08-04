# merge sort in python
    
print("factorial\n")

def factorial(x):

    if x == 1:
        return 1
        
    else:
        return (x * factorial(x-1))


n = int(input("Enter a no"))
ans = factorial(n)
print("The factorial of", n, "is", ans)