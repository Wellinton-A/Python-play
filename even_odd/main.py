

def evenOrOdd():
    list1 = [* range(int(input("First number of range: ")), int(input("Second number of range: "))+1, 1)]
    choose = (int(input("Choose \n 1 - Even \n 2 - Odd \n")))
    if choose == 1:
        for i in list1:
            if i % 2 != 0:
                list1.remove(i)
    elif choose == 2:
        for i in list1:
            if i % 2 == 0:
                list1.remove(i)
    else:
        print("invalid input!!!!!")
        list1.clear()
        evenOrOdd()
    print(*list1, sep="-")

def divisibleNumb():
    list2 = [* range(int(input("First number of range: ")), int(input("Second number of range: "))+1, 1)]
    divisibleNumber = int(input("Choose a number to be divisible: "))
    list3 = []
    for i in list2:
        if i % divisibleNumber == int(0):
            list3.append(i)
    print(*list3, sep="-")

def sumTotal():
    list2 = [* range(int(input("First number of range: ")), int(input("Second number of range: "))+1, 1)]
    total = 0
    for i in list2:
        total += i
    print(total)

def init():
    menu = int(input("WELCOME EVEN OR ODD RANGE\nCHOOSE:\n1 - EVEN OR ODD\n2 - DIVISIBLE NUMBER\n3 - SUM TOTAL\n"))
    if menu == 1:
        evenOrOdd()
    elif menu == 2:
        divisibleNumb()
    elif menu == 3:
        sumTotal()
    else:
        print("invalid value!!")
        init()

init()