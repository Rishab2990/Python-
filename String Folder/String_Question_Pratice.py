#Question - reverse a string
name = "Hello World"


print(name[::-1])
print(name[:5]) #0-4 element print  
print(name[::]) # all element printed 
print(name[1:5]) #1-4 element printed

print(name[5:1]) # it will not print anything because 5 is greater than 1
print(name[5:1:-1]) #for this code as a beginner first dry run it on paper and then you will understand it
# same normal count 0 to 5 and then from 5 start reverse count 5 to 1 with neative step -1 like first step is positive 5 and negative step -1 means positive negative answer is negative and value we get also negative means now 5 conver into 4 same for all logic and at the end stop at 1.
#  

print(name[11::-1])

[]