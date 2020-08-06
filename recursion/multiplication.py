print("table of a no")

def mul_table(n, i=1):
    print (n*i)
    if i != 10:
        mul_table(n,i+1)
        
no = int(input("enter a no \n"))
mul_table(no)