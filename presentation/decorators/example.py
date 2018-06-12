def my_decorator(some_function):
    def wrapper(*args, **kwargs):
        print("Do something before the function is called")
        some_function(*args, **kwargs)
        print("Do something after the function is called")

    return wrapper

@my_decorator
def addition(a, b):
    result = a+b
    print("Addition of {} and {} is {}".format(a,b,result))

if __name__ == "__main__":
    addition(3,4)