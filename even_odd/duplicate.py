list1 = ['a','b','c','d','d','d','d','e','f','f',1,1,2,2,3,4,5,1,6]

print(*list1)
list2 = []
for i in list1:
    if list2.count(i) < 1:
        list2.append(i)

print(*list2)

list3 = []
for i in list1:
    if list1.count(i) > 1:
        list3.append(i)

print(*list3)
