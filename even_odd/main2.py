dictionary = {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
}

my_list = [dictionary,
            {'a' : [1,2,3],
             'b' : 'hello',
             'c' : True,
             'd' : 'bye'}]

for i in my_list:
    for k, v in i.items():
        print(k,v, sep=" = ")

for i in my_list:
    for j in i.keys():
        print(j)

for i in my_list:
    for j in i.values():
        print(j)