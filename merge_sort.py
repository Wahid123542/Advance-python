list1=[1,2,3,4,5]
list2=[3,4,5,6,7,8,12,13]

list3=[]
len1=len(list1)
len2=len(list2)
i=j=0
while i<len1 and j<len2:
    if list1[i]<list2[j]:
        list3.append(list1[i])
        i=i+1
    else:
        list3.append(list2[j])
        j+=1
list3 +=list1[i:]
list3 +=list2[j:]

print(list3)
