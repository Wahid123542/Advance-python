#else runs only when the loop finishes without a break

_list=[2,4,1,2,4]

number=int(input("please enter a number"))

for i in _list:
    if number==i:
        print("found")
else:
     print("not found")


