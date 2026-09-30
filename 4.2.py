my_list = [6]

index_1 = []
item_1 = []
for index, item in enumerate(my_list):
    if index % 2 == 0:
        item_1.append(item)

if my_list:
    print(sum(item_1) * my_list[-1])
else:
    print(0)
