def sortStr(string):
    list = []
    str = ""
    for i in string:
        list.append(i)
    list.sort()
    return (str.join(list))

print(sortStr("bacde"))


