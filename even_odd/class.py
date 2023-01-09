class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self)


player1 = PlayerCharacter("Wellinton", 27)

print(player1.run())


# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# cat1 = Cat("kitty", 7)
# cat2 = Cat("blue", 6)
# cat3 = Cat("deus", 10)

# def older_cat(*args):
#     return max(args)

# print(f"The oldest cat is {older_cat(cat1.age, cat2.age, cat3.age)} years old")
