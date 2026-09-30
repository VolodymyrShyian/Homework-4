my_list = [0, 1, 0, 12, 3]

new_list = []
zero_list = []
for number in (my_list):
    if number!= 0:
        new_list.append(number)
    elif number == 0:
        zero_list.append(number)
print(new_list + zero_list)
