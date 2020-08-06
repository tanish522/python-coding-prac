print("sum off numbers from 1 to n")

def rec(n):
    if(n == 1 ):
        return 1
    else:
        return n+rec(n-1)
        
no = int(input("enter a no \n"))
print(rec(no))