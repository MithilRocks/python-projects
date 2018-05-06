from time import sleep

def Compute():
    for i in range(10):
        yield i
        sleep(0.5)

for val in Compute():
    print(val)