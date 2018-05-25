# OPERATORS 
# Arity, Precedance, Associativity

"""
Right to left associativity is for:
-Unary (!)
-Ternary (not in python)
-compound assignments (+=, -=) 

Rest all are left to right

-----------------------------------------------
On Python 2.7, 5/2 will give 2 
On Python 3.x, 5/2 will give 2.5

-----------------------------------------------
5//2 is floor division

-----------------------------------------------
Relational: >, <, >=, <=, <>, !=

On Python 2.7, <> works but not in 3.x

-----------------------------------------------
Logical: and, or, not
there is no xor

-----------------------------------------------
++x gives result but x++ will be an error.
++x is treated as binary

-----------------------------------------------
Homework: Find binaries of following numbers
13441, 1111, 65535, 221224 

-----------------------------------------------
1. Turn off bits:
01101100
11110011 and
------------
01100000

2. Turn on bits:
01100000
00001100 or
------------
01101100

3. Toggle bits:
01101100
00011110 xor
------------
01110010

4. Shifting: left shift
x = 10 00001010
x = x << 1 00010100 = 20
x = x << 1 00101000 = 40

It is incrementing by 10. Thus, this operation is multiplication of 2's power

x = x * 2 ^ power (power is left shift value)

5. Shifting: right shift
Similarly, right shift is division by 2's power
x = x/2^power (power is right shift value)

There are two types of right shifts
Logical right shift: 0 gets added
Arithmatic right shift: 1 gets added

Negative numbers are stored in binary in 2's compliment form. 
2's compliment form = 1's compliment (toggle) + 1
---------------------------------------------------

HomeworK: find out binary of
-32, -1, -255, -483

6. Compliment:
~ represents compliment

----------------------------------------------------

Python has added two membership operators: in and not in
Also is and not is
say,
x= 1000
y=x
z=1000

x and y have same memory address but z is different.
so x is y will be true. x is z will be false.
"""
