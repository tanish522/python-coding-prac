# stack using deque

from collections import deque

stack = deque() 
  
# append() function to push element in the stack 
stack.append("1") 
stack.append("2") 
stack.append("3") 
  
print('Initial stack:') 
print(stack) 
  
# pop() fucntion to pop element
print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
print(stack) 