#!/usr/bin/python
'''
In 2.7 there's raw_input() and in 3.x there's input. both take input as string.
Likewise, in 2.7 input() takes input as it is. ie it treats integers as integers and so on. 
In 3.x we have eval(input()) that takes input as string and converts it to the appropriate container type. 
Take care that if you want to enter string using this in 2.7, use quotation marks as well.
'''
a = input("Enter a number: ")
print(a, type(a)) #a is treated as string even when a number is entered.

b = int(input("Enter a number: "))
print(b, type(b)) #b is treated as int as it converts it to integer

'''
String slicing is important.
One of the most important things first asked in Python interviews
Slicing method is given as follows x[ [ start-index ] : [ end-index ] [ : step-index ] ]
Start-index is the place to start slicing. It is inclusive.
End-index is the place to stop slicing. It is exclusive.
Step-index increments start-index by the step-index number

if x = "Hello"
this is how the string is indexed:

H  e  l  l  o
0  1  2  3  4
-5 -4 -3 -2 -1

These are the positive and negative indexes assigned

So x[1:4:2] will give 'el'
It starts at index 1 ie 'e'. It steps 2 ie 1+2=3. Third index is the second 'l'.
After incrementing step again 3+2 = 5 we see that we have gone past the end-index so the slicing stops.

x = x[:] = x[::]

x[:] in this the start-index is 0 and end index is the length of the string. 
x[::] in this start and end indexes are the same as above. the step index is considered 1. 
Step index is always optional but when specified, it can never be 0

if step index is positive then start index should always be smaller than end index otherwise we won't get anything.
if step index is negative then start index should always be greater than end index otherwise we won't get anything.

x[::-1] traverses the string in reverse order

Questions:
1. c[6::-1] and c[6:0:-1] give different result. What is the end index considered as?
'''
c = "Mithil Bhoras"
print(c[1:4:2]) #result is 'ih'
print(c[5:4:-2]) #result is 'l'

