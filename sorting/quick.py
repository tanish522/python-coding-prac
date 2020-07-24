# merge sort in python
    
print("quick sorting\n")
arr=[]
n= int(input("enter no of elements\n"))
print("enter elements\n")

for i in range(n):
    data=int(input())
    arr.append(data)


def partition(arr,l,h):
    i= l-1
    pivot = arr[h]
    for j in range(l , h):     
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i=i+1
            # swapping
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return ( i+1 ) 
        
def quickSort(arr,l,h): 
    if l < h:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr,l,h)
        # Separately sort elements before partition and after partition
        quickSort(arr, l, pi-1) 
        quickSort(arr, pi+1, h) 

# Driver code to test above 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])