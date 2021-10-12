
print("second greatest\n")
a=[]
n= int(input("enter no of elements"))
print("enter elements")

for i in range(n):
 data=int(input())
 a.append(data)
 
for i in range(0,n):
    for j in range(0,n-1):
        if a[j] > a[j+1]:
         tmp=a[j]
         a[j]=a[j+1]
         a[j+1] = tmp
    
print(a[-2])
