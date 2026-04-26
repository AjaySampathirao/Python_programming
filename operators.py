#!/bin/python3

#Arithmetic_operators
print("Arithmetic_operators")

#Variables
a=15
b=4
print(f"a={a}")
print(f"b={b}")

#Addition
print(f"Addition(+):{a+b}")

#Subtraction
print(f"Subtraction(-):{a-b}")

#Multiplication
print(f"Multiplication(*):{a*b}")

#Division
print(f"Division(/):{a/b}")

#Floor Division (remove decimals ex:3.75 Ans:3)
print(f"Floor Division(//):{a//b}")

#Modulus (Remainder Value)
print(f"Modulus(%):{a%b}")

#Exponentation (Power value)
print(f"Exponentation(**):{a**b}")
print("\n")

#Comparision_operators
print("Comparision_operators")

a=13
b=33
print(f"a={a}")
print(f"b={b}")

print(f"Graterthen(>):{a>b}")
print(f"Lessthen(<):{a<b}")
print(f"Equal(==):{a==b}")
print(f"Notequal(!=):{a!=b}")
print(f"Graterthenequal(>=):{a>=b}")
print(f"Lessthenequal(<=):{a<=b}")
print("\n")

#Logical_operators
print("Logical_operators")

a=True
b=False
print(f"a={a}")
print(f"b={b}")

print(f"and:{a and b}")
print(f"or:{a or b}")
print(f"not:{not a}")
print("\n")

#Bitwise_operator
print("Bitwise_operator")

a=10
b=14
print(f"a={a}")
print(f"b={b}")

print(f"Bitwise AND(&):{a&b}")
print(f"Bitwise OR(|):{a|b}")
print(f"Bitwise NOT(~):{~a}")
print(f"Bitwise XOR(^):{a^b}")
print(f"Left shift(<<):{a<<2}")
print(f"Right shift(>>):{a>>2}")
print("\n")

#Assignment_operator
print("Assignment_operator")

a=10
b=a
print(f"a={a}")
print("b=a")

print(f"Assignment(=):{b}")

b += a
print(f"Addition Assignment(+=):{b}")

b -= a
print(f"Subtraction Assignment(-=):{b}")

b *= a
print(f"Multiplication Assignment(*=):{b}")

b <<= a
print(f"Leftshift Assignment(<<=):{b}")
print("\n")

#Identity_operator
print("Identity_operator")

a=10
b=20
c=a
print(f"a={a}")
print(f"b={b}")
print("c=a")

print(f"a is not b:{a is not b}")
print(f"a is c:{a is c}")
print("\n")

#Membership_operator
print("Membership_operator")

x=24
y=20
print(f"x={x}")
print(f"y={y}")
list=[10,20,30,40,50]
print(f"list={list}")

if (x not in list):
 print("not in:x is not in given list")
else:
 print("in:x is present in given list")

if (y in list):
 print("in:y is in the given list")
else:
 print("not in:y is not in present given list")
print("\n")

