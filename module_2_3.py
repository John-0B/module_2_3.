index = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while len(my_list) > index:
    number = my_list[index]
    index = index + 1
    if number == 0:
        continue
    elif number < 0:
        break
    print(number)
