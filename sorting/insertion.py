# insertion sort in python
    
print("insertion sorting\n")
a=[]
n= int(input("enter no of elements"))
print("enter elements")

for i in range(n):
    data=int(input())
    a.append(data)
print(a)

#sorting
for i in range(1,n):
    tmp=a[i]
    j=i-1
    while j>=0 and a[j]>=tmp:
        a[j+1]=a[j]
        j-=1
        
    a[j+1]=tmp
    
for i in range(n): 
    print(a[i])