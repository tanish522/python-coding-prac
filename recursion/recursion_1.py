
print("Sum of all the numbers from 0 to n")

def summ(n):
    if n== 0:
        return 0
    else:
        return n + summ(n-1)

a = int(input("enter number\n"))

for i in range(0,a):
    print(summ(i))