# Another method of printing statements

name = "mithil"
last_name = "bhoras"

print("Your first name is {} and last name is {}".format(name.upper(), last_name.upper()))

# you can specify indexes in the brackets!

print("Your last name is {1} and first name is {0}".format(name.upper(), last_name.upper()))

# Program: Write a program to accept string from user and return a result string which is made of first two
# and last two characters

def firstandlasttwo(input):
    return input[:2]+input[-2:]

# Write a program to accept count of donuts from user
# if the count is less than 10, output should be number of donuts:what ever count user has entered
# if count is more than 10, print "many"

def donunts(num):
    result = "Number of donuts: "+str(num)
    if num>10:
        result = "Number of donuts: Many"
    return result

# HW: Write a program to accept a number from user and print if it is divisible by 
# 2,3 or 5 and divisible by any two numbers (2,3 or 2,5 or 3,5)

def check_divisibility(num):
    result = "Number is divisible by "
    if num % 2 == 0:
        result += "2 "
    if num % 3 == 0:
        result += "3 "
    if num % 5 == 0:
        result += "5 "
    return result

# Write a program to accept a line from user. If length of the line is less than 20 
# then output should be "You entered a very short line". If it is between 20 to 80, 
# output should be "Line contains sufficient number of characters". If more than 80,
# output should be "Line length exceeded"
def check_line_length(string):
    result = ""
    if len(string) < 20:
        result = "You entered a very short line"
    elif len(string) >= 20 and 80 >= len(string) :
        result = "Line contains sufficient number of characters"
    else:
        result = "Line Length exceeded"

    return result

# Write a program to accept marks of six subjects. Find out percentage out of it. All 
# marks are out of 100. Based on percentage, display whether student has 
# secured distinction, higher second class, second class, pass with atkt, fail

""" 
Loops
"""

""" 
while <condition>:
    <stmts to execute while condition is not false>
else:
    <execute if while terminates. this is optional>

Python has else for while wow!
"""

# HW: WAP to accept a number from user and stop when user enters multiple of 11.

def whileLoop():
    no = 1
    while no != 0:
        no = eval(input("Enter Number, to stop enter 0: "))
        print("You entered "+str(no))

# Wap to accept a string from user and find out it's length without using buit in function

def MyLen(string):
    len = 0
    try:
        while string[len] != "\0":
            len += 1
    except:
        pass
    return len

def myOtherLen(string):
    len = 1
    while string[:len] != string:
        len += 1
    return len

# HW: WAP to accept a string from user and accept a character whose occurence is to be counted
# in the given string. Don't use built in funcition
def checkOccurrences(string, character):
    count = 0
    ind = 0
    try:
        while string[ind]:
            if string[ind] == character:
                count += 1
            ind += 1
    except:
        pass
    return count

# HW: WAP to accept a string from user. Accept start index, end index and step index.
# Define your own slice function
def mySlice(string, start, end, step):
    result = ""
    ind = start
    if step > 0:
        while ind < end:
            result += string[ind]
            ind += step
    elif step < 0:
        while ind > end:
            result += string[ind]
            ind += step
    return result

# HW: WAP to accept a number from user and display it's reverse. Don't use splice
def reverse_string(string):
    ind1 = -1
    result = ""
    try:
        while string[ind1]:
            result += string[ind1]
            ind1 -= 1
    except:
        pass
    return result

# HW: WAP to check palindrome
def palindrome(string):
    if string == reverse_string(string):
        return "Yes"
    return "No"

if __name__ == "__main__":
    string = input("Enter a string: ")
    # print("updated sting is {}".format(firstandlasttwo(string)))

    # num_of_donuts = eval(input("Enter number of donuts: "))
    # print(donunts(num_of_donuts))

    # whileLoop()

    print("String length is: "+str(MyLen(string)))
    print("String length is: "+str(myOtherLen(string)))
    print("Reverse of string '{}' is '{}'".format(string, reverse_string(string)))
    print("Is '{}' a palindrome: {}".format(string, palindrome(string)))
    print(check_line_length(string))

    num = eval(input("Enter a number to check if it is divisible by 2, 3, 5: "))
    print(check_divisibility(num))

    # start = eval(input("Enter Start Index: "))
    # end = eval(input("Enter End Index: "))
    # step = eval(input("Enter Step value: "))

    # print("Your sliced string is '{}'".format(mySlice(string,start,end,step)))

    # character = input("Enter a single character whose number of occurences to check in string: ")
    # print("Number of times '{}' came in '{}' is {}".format( character, string, checkOccurrences( string, character ) ) )
