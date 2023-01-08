
def highestEven(li):
    li2 = []
    for i in li:
        if i % 2 == 0:
            li2.append(i)
    return max(li2)



list1 = [1,2,3,48,49,6,7,8,9,10]
print(highestEven(list1))