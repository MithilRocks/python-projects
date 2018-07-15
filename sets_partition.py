example_set = {1,2,3,4,6,10,12,34,22}
num = 22

temp_num = num
my_set = set()

while True:
    if temp_num in example_set:
        my_set.add(temp_num)
        temp_num -= 1
    else:
        print(my_set)
        my_set = set()
