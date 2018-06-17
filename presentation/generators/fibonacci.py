def fibonacci(n):
    x, prev = 0, 1
    for i in range(1,n):
        yield x
        temp = x
        x = x + prev
        prev = temp

for j in fibonacci(10000):
    print(j)
