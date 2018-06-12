def multiply_num(a, b, c = 1, d = 1, e = 1):
    return a*b*c*d*e

def add_num(a, b, c = 0, d = 0, e = 0):
    return a+b+c+d+e

def add_any(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

def factorial(num):
    if num > 0:
        return num * factorial(num - 1)
    else:
        return 1

def add_int(*args):
    sum = 0
    for x in args:
        if x.isdecimal():
            sum += x
    return sum

def demo(a, b, *args, **kwargs):
    for x in args:
        print(x)

    for x in kwargs:
        print(x, kwargs[x])

if __name__ == "__main__":
    # write a function which can multiply 2,3,4 or 5 numbers
    print("Addition of numbers: ",add_num(2,3,100,2,3))
    print("Multiplication of numbers: ",multiply_num(2,3,100,2,3))

    # a function that takes as many number of arguments as it can
    print("Addition of n numbers: ",add_any(1,2,4,5,12,3,70))

    # HW: WTP which accepts heterogeneous variable number of arguments and returns sum of integers from the argument 
    # list  
    # print("Addition of integers: ",add_int(2, 3, "hello"))

    demo(1,2,3,4,5,6,7,name="mithil",hobby="films")

    # HW: WTP to accept three numbers and check if those numbers can result into forming a triangle
    # HW: WTP to accept a number from user and print sum of the digits of the given number
    # HW: WTP to accept a number from user and and display single digit sum of the given number
    # HW: WTP to accept a number from user and check if it is a special number (cubes of the digits sums is the same
    # number)
    # HW: WTP to accept a number from user and display odd digits and even digits sums. don't use any arithmatic operator to use