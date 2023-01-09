
def highestEven(li):
    highest = 0
    for i in range(1, len(li)):
        for j in range(0, len(li)):
            if li[j] > li[i] and  li[j] % 2 == 0:
                highest = li[j]
    return highest






list1 = [1,2,3,48,49,6,7,8,9,10]
print(highestEven(list1))