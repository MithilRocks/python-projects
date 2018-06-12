import time
from example import my_decorator

def time_taken(func):
    def ret_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs) 
        end = time.time()
        print(func.__name__ + " takes time: " + str( (end - start) ) + " milli seconds")
    return ret_func

@time_taken
@my_decorator
def count_numbers(num):
    print("In Count Numbers")
    for i in range(num):
        pass

if __name__ == "__main__":
    count_numbers(1000000)