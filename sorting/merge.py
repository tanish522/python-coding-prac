# merge sort in python
    
print("merge sorting\n")
arr=[]
n= int(input("enter no of elements\n"))
print("enter elements\n")

for i in range(n):
    data=int(input())
    arr.append(data)


def sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l = arr[ :mid]
        r = arr[mid: ]
        
        sort(l) #sort first half
        sort(r) #sort second half
        
        i=j=k=0
        # Copy data to temp arrays l[] and r[] 
        while i < len(l) and j < len(r):
            if l[i] < r [j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        
        # for last element which was left
        while i < len(l): 
            arr[k] = l[i] 
            i+= 1
            k+= 1
          
        while j < len(r): 
            arr[k] = r[j] 
            j+= 1
            k+= 1
        
# Code to print the list 
def printList(arr): 
        print(arr) 
        
# driver code to test the above code 
print("Given array is \n")  
printList(arr) 
sort(arr) 
print("Sorted array is: \n") 
printList(arr)