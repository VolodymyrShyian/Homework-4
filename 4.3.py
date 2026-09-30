import random
my_list = random.sample(range(1,100), random.randint(3 ,10))
print(my_list)
new_list = [my_list[0], my_list[1], my_list[-2]]
print(new_list)