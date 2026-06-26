import sys


print("Hello, World!")

a = 5
print(sys.getrefcount(a))


5
print(sys.getrefcount(5))


# c = 24601
# print(sys.getrefcount(c))

print(sys.getrefcount(24601))


#let suppose we have a data like a = 5 
# in which if variable have no power no object  holding no datatype holding only reference 
# means this variable "a" just work like a arrow which point to the object 5 and 
# this object 5 is hold by the memory and this object 5 have a datatype int
# now the question is if variable "a" is just a reference then would be use any value any sign or anything as a variable name
# the answer is no because variable name must be a valid identifier in python and it should follow the rules of naming variables in python
# for example we can't use 1a or @a or #a as variable name because they are not valid identifiers in python but we can use a1 or a_1 or _a as variable name because they are valid identifiers in python

"""Object's datatype is hold by the memory not the variable is just a reference which point the object means
   memory hold both object and its datatype """

#Better Version 
""" In Python, variables do not directly store values or datatypes.

A variable is just a reference that points to an object in memory.

The object stored in memory contains both:
1. the actual value
2. the datatype information"""


#rules for naming variables in python
#1. variable name must start with a letter or underscore
#2. variable name can only contain letters, numbers and underscores
#3. variable name cannot be a reserved keyword in python
#4. variable name cannot start with a number
#5. variable name cannot contain spaces




myListOne = [1, 2, 3, 4, 5]      
myListTwo = myListOne     #both myListOne and myListTwo are pointing to the same object in memory which is [1, 2, 3, 4, 5].
                          #not creating a new object in memory for myListTwo but just pointing to the same object in memory

print(myListOne)
print(myListTwo)
print("memory address of myListOne:",id(myListOne)) #id() function in python which returns the memory address of the object in memory
print("memory address of myListTwo:",id(myListTwo)) #both myListOne and myListTwo are pointing to the same object in memory 
                                                    #which is [1, 2, 3, 4, 5] and both have the same memory address

myListOne[3]=555
print(myListOne)
print(myListTwo)

#In this above code the value of myListOne is changed but the value of myListTwo is also changed because both myListOne and myListTwo 
# are pointing to the same object in memory which is [1, 2, 3, 4, 5] and when we change the value of myListOne then it also change 
# the value of myListTwo because both are pointing to the same object in memory.



#Another example of this is
mylistone=[10,20,30,40,50]
mylisttwo = mylistone
print("mylistone:",mylistone)
print("mylisttwo:",mylisttwo)

mylistone=[100,200,300,400,500]
print("mylistone:",mylistone)
print("mylisttwo:",mylisttwo)

#In this above code the value of mylistone is changed but the value of mylisttwo is not changed because when we assign 
# a new value to mylistone then it creates a new object in memory and mylistone now points to the new object and mylisttwo 
# still points to the old object in memory which is [10, 20, 30, 40, 50] and when we change the value of mylistone then it 
# does not change the value of mylisttwo because they are pointing to different objects in memory.


#Both the above examples are showing the concept of mutable and immutable objects in python.
#In the first example we are using a list which is a mutable object in python and in the 
#second example we are using a list which is also a mutable object in python but when we assign a new value to mylistone
#Then it creates a new object in memory and mylistone now points to the new object and mylisttwo still points to the old 
#Object in memory which is [10, 20, 30, 40, 50] and when we change the value of mylistone then it does not change the value of 
#mylisttwo because they are pointing to different objects in memory.

#New example 

h1=[11,22,33,44,55,45]
h2=h1[:] 
print("memory address of h1:",id(h1))
print("memory address of h2:",id(h2))
""" this is called slicing and it creates a new object in memory which is a copy of the original list h1 and h2 
 now points to the new object in memory which is a copy of the original list h1. to understand this concept better we 
 can use the id() function in python which returns the memory address of the object in memory 
 and also refer line number 51 to 52 how normal code work and slicing code work """
