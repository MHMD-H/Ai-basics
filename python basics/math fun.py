#built in function

#1.max() & min()
x=[44,23,78,99,10,23]
print(max(x)) #99
print(min(x))#10

#2.round --> remove digits round(num,num of digits)
y = 6.98345
print(round(y,2))#6.98
print(round(y)) #7

#3.pow() ---> pow(num,power)
print(pow(5,3))#125

#4.abs() --> absoulate value
print(abs(-9))#9

#--------------------------------------------

#math library

import math

#1. math.pi ---> 3.14 or 22/7

reduis = 7
perimeter = 2*math.pi*reduis
print(round(perimeter)) #44

#2. math.ceil() --> بتقرب الرقم لاكبر عدد صحيح
#2. math.floor() --> بتقرب الرقم لاصغر عدد صحيح
z = 9.1
print(math.ceil(z))#10
print(math.floor(z))#9

#3. math.sqrt() ---> square root
a = 25
print(math.sqrt(a)) #5

#4math.factorial() --->Returns the factorial of a number
n=7
print(math.factorial(n))#5040

#5. math.sin(), math.cos() , math.tan()

theta =  90
print(math.sin(math.radians(theta)))
print(math.cos(math.radians(theta)))
print(math.tan(math.radians(theta)))


