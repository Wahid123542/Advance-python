#How to send a function as a argument to another function in python
def square(n):
  return n*n 

def first_class_function(func, list):
  result=[]
  for i in list:
    result.append(func(i))
  return result
print(first_class_function(square,[1,2,3]))
