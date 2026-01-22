#Generators in python
def my_generator(limit):
  for i in range(limit):
    yield i

x=my_generator(5)
print(next(x))
print(next(x))
