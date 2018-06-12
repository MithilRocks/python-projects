def table(lb, ub):
    for i in range(lb, ub+1):
        print("The table of %d is: " %(i))
        for j in range(1,11):
            print("%d * %d = %d" %(i, j, i*j))

def main():
    lb = eval(input("Lower bound is: "))
    ub = eval(input("Upper bound is: "))

    table(lb,ub) # this is the positional arguments 
    table(ub = 15,lb = 2) # key word parameters, you are directly assigning to keywords
    table(ub = ub,lb = lb) # this works. python is smart enough to distinquish

if __name__ == "__main__":
    main()