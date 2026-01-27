_list = [3, 4, 3, 5, 8, 6, 9, 7]
length=len(_list)
print(length)
for i in range(1,length):
    for j in range(i):
        if _list[j]>_list[i]:
            temp=_list[i]
            del _list[i]
            _list.insert(j,temp)
            break
        
print(_list)
