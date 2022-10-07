from os import name


def make_list(number):
    names = []
    for item in range(number):
        names.append(input("enter:"))
    return names


number = int(input("number enter:"))
names = make_list(number)
for name in names:
    if name[0] == "A":
        print(name)
