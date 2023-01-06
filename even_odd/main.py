
print("WELCOME EVEN OR ODD RANGE")

def evenOrOdd():
    list1 = [* range(int(input("First number of range: ")), int(input("Second number of range: ")), 1)]
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
        list1 = []
        evenOrOdd()
    print(*list1, sep="-")

evenOrOdd()