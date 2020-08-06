print("sum off all odd numbers from 1 to n")

def rec(n):
    if(n == 1 ):
        return 1
    else:
        return n+rec(n-2)
        
no = int(input("enter an odd no \n"))
print(rec(no))