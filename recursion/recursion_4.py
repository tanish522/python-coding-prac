print("sum off all even numbers from 0 to n")

def rec(n):
    if(n == 0 ):
        return 0
    else:
        return n+rec(n-2)
        
no = int(input("enter an even no \n"))
print(rec(no))