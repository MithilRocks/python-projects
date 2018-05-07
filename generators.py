from decorators import time_taken

@time_taken
def firstn(n1,n2):
    num = n1
    while num < n2:
        yield num
        num += 1

print(sum(firstn(100,1000)))