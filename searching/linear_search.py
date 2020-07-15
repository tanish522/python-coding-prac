# Hello World program in Python
    
print "Hello World!\n"
a=[1,5,10,20,40,50,100]
key = input("enter key :")

for x in a:
 if key == x:
  print("key is present at ",a.index(x)+1)
  flag=1
  break
 else:
  flag=0
 
if flag == 0:
 print("key not found")
