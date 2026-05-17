import math
import random
from decimal import Decimal


a = 5
b = 10
c = 15
print(a+b*c) #Before writing this kind of code we have to understand operator precedence
             #In this case, multiplication has higher precedence than addition, so it will be evaluated first.
             #Now the Question is what if we want to change the order of evaluation? for this we can use parentheses to 
             # explicitly specify the order of operations. For example:
print((a+b)*c) 
#In this case, the addition will be evaluated first because it is enclosed in parentheses, and then the result will be multiplied by c.


a1 = 20
new_Value = float(a1) #This will convert the integer value of a1 to a floating-point number.
print(new_Value) #Output: 20.0

b1 = 3.14
new_Value_B = int(b1) #This will convert the floating-point value of b1 to an integer.
print(new_Value_B) #Output: 3   


print(2**10000) #This will calculate 2 raised to the power of 10000, which is a very large number. Python can handle large integers, 
#so it will return the result without any issues.   

print(1000**1000) #This will calculate 10000 raised to the power of 10000, which is an even larger number. Python can still handle this,





repr("Hello, World!") #This will return a string representation of the object "Hello, World!" which includes the quotes. 
#The output will be: "'Hello, World!'"

str("Hello, World!") #This will return a string representation of the object "Hello, World!" without the quotes.

print(str("Hello, World!")) #Output: Hello, World!
print(repr("Hello, World!")) #Output: 'Hello, World!'
print("Hello, World!") #Output: Hello, World!



print(a<b<c) #This check if a is less than b and b is less than c, which is true, so it will return True.
              #But this is not the best way to check it may   create consusion as begineer 

# Python supports chained comparisons.
# This checks:
# (a < b) and (b < c)
#
# Beginners may find this syntax confusing at first,
# so the expanded version below may feel easier to read initially.
print(a<b and b<c)
print((a<b) and (b<c)) #This is the best way to check if a is less than b and b is less than c, which is true, so it will return True.


comparison = (5==10) and (10<15)
print(comparison)

print(math.floor(6.5)) #floor function always return integer value in output not matter what the input is . 
print(math.floor(-6.5)) #Output: -7 because floor function when the input is negative it will always return value negative value but in negative increasing order like -7, -8, -9 and so on.


#ceil function is wise version of floor function because it will always return the smallest integer greater than or equal to the input value.
print(math.ceil(6.5)) #Output: 7 because ceil function will return the smallest integer greater than or equal to 6.5, which is 7.
print(math.ceil(-6.5)) #Output: -6 because ceil function will return the smallest integer greater than or equal to -6.5, which is -6.


#iota numbers
iota = 1 + 2j  # This creates a complex number with real part 1 and imaginary part 2
print(iota)

iota_numbers = (3+4j)*10 #
print(iota_numbers) #This will multiply the complex number (3+4j) by 10, resulting in (30+40j).



print(int("64" , base=8))#This will convert the string "64" to an integer using base 8 (octal). 


print(random.random())
print(random.random())
print(random.random())

print(random.randint(10,100))
print(random.randint(5, 500))


print(random.choice(['apple', 'banana', 'cherry', 'date', 'fig', 'grape'])) #This will randomly select and return one element from 
 #the list of fruits provided. Each time you run this code, it may return a different fruit from the list.


shuffle_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(shuffle_list) #This will randomly shuffle the elements of the list shuffle_list in place, meaning that the original list will be modified to contain the shuffled order of the elements.
print(shuffle_list) #Output: The output will be a randomly shuffled version of the original list [1,2,3,4,5,6,7,8,9,10]. Each time you run this code, the order of the elements in the list will be different due to the random shuffling process.


print(print("Hello, World!")) #This will print "Hello, World!" and then return None because the print function does not return any value.
#this code output will be: first thing always be understand the python look innermost paranthese first and then move outward 
#this is what happens in the previous shuffle related code 








#Decimal context manager in python #Import to read about it in python documentation

number1 = 0.1+0.1+0.1
print(number1)

number2 =0.1+0.1+0.5+0.2
print(number2)

number3 = 0.1+0.1+0.1-0.3
print(number3)


