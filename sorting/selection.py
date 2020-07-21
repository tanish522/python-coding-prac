# selection sort in python
    
print("selection sorting\n")
a=[]
n= int(input("enter no of elements"))
print("enter elements")

for i in range(n):
    data=int(input())
    a.append(data)
print(a)

#sorting
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if a[min] > a[j]:
            min=j
        
    tmp=a[min]
    a[min]=a[i]
    a[i]=tmp
    
for i in range(n): 
    print(a[i])