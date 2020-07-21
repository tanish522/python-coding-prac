# binary search 
    
print "Hello World!\n"
a=[1,5,10,20,40,50,100]
key = input("enter key :")
low=0
high=6
flag=0

while low<=high:
 mid=(low+high)/2
 if key == a[mid]:
  print("key is present at ",mid)
  flag=1
  break
 elif key<a[mid]:
  high=mid-1
 else:
  low=mid+1
 
if flag == 0:
 print("key not found")
