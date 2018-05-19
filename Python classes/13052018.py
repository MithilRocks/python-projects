'''
string methods
'''

c = "hello world"

print(c.capitalize()) #capitalizes the first letter. doesn't change original variable

print(c.count('l',0,3)) #searches substring. can specify start and end and it'll search only with in that range

print(c.center(23,'*')) # makes the string of length 23 by appending the character specified in both ways

print(c.upper()) # convert to uppercase

'''
Assignment: write your own center method that'll append two different characters at start and end
'''
""" input_string = input("Enter string to center: ")
first_string = input("Enter first string to pad at beginning: ")
last_string = input("Enter first string to pad at ending: ")
length_string = int(input("Enter length of centered string: "))

if len(input_string) < length_string:
    difference = length_string - len(input_string)

    if difference % 2 == 0:
        equal_input = difference/2
        input_string = equal_input*first_string + input_string + equal_input*last_string

print(input_string) """
'''
Assignment end
'''

print(c.find('ll',2,6)) # find substring in between optional start and end. returns start index of the substring

print(c.index('e', 1, 5)) # almost same as find but returns error 'substring not found' upon execution

print(c.rfind('ll', 1, 5)) # finds the highest index of the substring in the string

print(c.upper()) # enter string to upper

'''
Assignment: Write a program to accept a string from user and accept another string whose all search indexes 
should be printed
'''
""" print("My find function: ")
input_string = input("Enter search string: ")

x = "absdlfkjsldablsjdflab"
index = 0
indexes_list = []
while index != -1:
    index = x.find(input_string, index)
    if index != -1:
        indexes_list += [index]
        index += len(input_string)

print(indexes_list) """
'''
Assignment end
'''

'''
Write a program to accept a string from user and swap the cases
'''
""" swap_case_string = input("Enter String whose cases you wanna swap: ")
print(swap_case_string.swapcase()) """


'''
Write a program to accept an input string and ends with string. check if first string ends with second string.
'''
""" your_string = input("Input your string: ")
end_string = input("Input String to check whether it is at the end of previous string: ")
if your_string.endswith(end_string) == 1:
    print("%s is at the end of %s" %(end_string, your_string)) """


'''
Write a program to accept a string from user and to replace occurences of first character in the remaining string with star
'''
input_string = "ababdgklkjlabablskjab"
print(input_string[0]+input_string[1:].replace(input_string[0], '*'))
'''
end
'''

# String is immutable. You cannot do x[0] = 'x'

user_string = input("Enter your string: ")
'''
write a program to accept a string from user and print count of vowels in it
'''
vowel_count = 0
for x in user_string:
    if x in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print("Vowel Count is: %d" %(vowel_count))



'''
write a program to accept a string from user and display all digits from it
'''



'''
write a program to accept a string from user and check if it is palindrome or not
'''
user_input = input("Enter to string for palindrome check: ")
if user_input[::-1] == user_input:
    print("You entered a Palindrome")



'''
write a program to accept a sentence from user. if the given sentence contains "not bad" replace with "good"
'''
user_input = input("Enter string: ")
print(user_input.replace("not bad", "good"))

