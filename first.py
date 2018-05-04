# this is the main py file. import other files to use their functionalities
from sort_list import Sort, Quick_sort

# usage of sorting 
def sort_example():
    a = Sort([2,9,1,45,23,12,89,34,9,99,1000,978,99,67,23,45])
    print(a.bubble_sort())

def class_inheritence_example():
    b = Quick_sort([2,9,1,45,23,12,89,34,9,99,1000,978,99,67,23,45])
    print(b.quick_sort())


class_inheritence_example()
