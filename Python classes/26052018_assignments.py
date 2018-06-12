# Function to find maximum of four numbers

def maximum(a, b, c, d):
    if a>b and a>c and a>d:
        print(a,"is the greatest")
    elif b>c and b>d:
        print(b,"is the greatest")
    elif c>d:
        print(c,"is the greatest")
    else:
        print(d,"is the greatest")

def change_suffix(string):
    result = string
    if string.endswith("ly"):
        result = string[0:-2]+"ing"
    elif string.endswith("ing"):
        result = string[0:-3]+"ly"
    return result

if __name__ == "__main__":

    string = input("Enter string: ")

    print("You entered {} and the result is {}".format(string,change_suffix(string)))

    a = eval(input("Enter a: "))
    b = eval(input("Enter b: "))
    c = eval(input("Enter c: "))
    d = eval(input("Enter d: "))

    maximum(a,b,c,d)