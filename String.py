#Python String is sequence of character and it is immutable in nature which means 
# we cannot change the value of string once it is created.

name = "John Doe"

#Slicing a string
print(name[0]) #Output: J
print(name[1]) #output: o
print(name[2]) #Output: h
print(name[3]) #Output: n

print(name[:]) #
print(name[0:4])

#negative indexing in python

#In negative indexing never start with -0 because 0- is same as 0 and it will give me the same output as positive indexing
#In negative indexing we start with -1 which is the last character of the string and the we move backwards to the first character
print('negative indexing',name[-1])   #Indexing starts from the end of the string and goes backwards
print('negative indexing',name[-2])
print('negative indexing',name[-3])
print('negative indexing',name[-4])
print('negative indexing',name[-5])
print('negative indexing',name[-6])
print('negative indexing',name[-7])
print('negative indexing',name[-8])

print(name[-2:-5])  # for this code the output will be empty string because when the code starts from negative index -2 and
# ends in -5, but those numbers are just positions and in the code have  not defined  specified steps. By default, Python takes\
#  steps in  the positive direction like +1. through this approach we cannot get the desired output only moving toward the positive direction.


print(name[-2:-5:-1]) # for this code the output will be 'oD' because when the code starts from negative index -2 and steps are also
# defined in negative direction -1, so the simple math applied like -2-1=-3 and again for next step -3-1=-4 and so on this is just a
# vise versa of previous code "line number 25" because in this step we have defined the steps in negative direction


print(name[-5:-2:1]) # this code is same as previous one "line number 25" because this code and previous code do same work but 
# in this we just defined the step in positive direction when we not defined steps then by default it takes steps in positive directoin 

print(name[0:-5])

print(name.upper()) # this code will convert all the characters of the string into uppercase letters
print(name.lower()) # this code will convert all the characters of the string into lowercase letters


#strip()
random_string = "   Hello World!   "
print(random_string.strip()) # this code will remove the leading and trailing whitespace from the string

#In this code internally in memory when we create variable random_string and assign value that time new variable create and start point to the 
#the object in memory and after this when we code print function then it use new memory space because string is immutable in python
#so when we use strip() method it will create new object in memory but after printing statement python immediately delete that
#object from memory because we have not assigned a variable to the new object created by strip() method .

#replace() method
print(random_string.replace("World!","Programmers"))

#python splitter() method
sentence = "Hello World! Welcome to Python programming."
print(sentence.split()) # this code will split the sentence into a list of words based on whitespace by default
print(sentence.split("o")) # this code will split the sentence into a list of words based on the character "o" as a delimiter
#In this code after printing statement python immediately delete the list created by split() method from memory because we have 


#find() method
print(sentence.find("World")) 

#count() method
print(sentence.count("o"))