# a decorator is used to create code that will be executed for functions
# the following function calculates the execution time of a function

import time
def time_taken(func):
    # accept the function as an argument
    def ret_func(*args, **kwargs):
        start = time.time()
        # call the function and pass all the necessary arguments
        ret = func(*args, **kwargs) 
        end = time.time()
        print(func.__name__ + " takes time: " + str( (end - start) ) + " milli seconds")
        # return function result
        return ret
    # return the time difference return
    return ret_func

print(__name__)