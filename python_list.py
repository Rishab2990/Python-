# a list is built-in data structure in python that is used to store collection of items. It is a mutable/changeable , allow duplicate
# and ordered collection of items. we use square brackets[] to define a list 

tea_varities = ["green tea", "black tea", "oolong tea", "white tea", "herbal tea"]
print(tea_varities)  

#print specfic element from the list
print(tea_varities[2])

print(tea_varities[1:2])



#Adding element to a list
tea_varities.append("chamomile tea") # this code will add "chamomile tea" to the end of the list
print(tea_varities,"\n")


#There is multiple way to add element in list 1. append() , 2. extend() , 3.insert() , 4. concatenation
#copy()  of list create a new list with different memory address and original list remain unchanged

animal_names_list = ["cat", "dog", "rabbit", "hamster","tiger","lion"]
print("original list memory address : " ,animal_names_list, "\n", "Original list memory address:", id(animal_names_list) , "\n")

slice_list = animal_names_list[2:5]  
print("slice list :  ", slice_list , "\n"  "Slice list memory address : " , id(slice_list) ,  "\n\n")


concatenated_list = animal_names_list+["giraffe", "elephant"]
print("concatenated list :", concatenated_list, "\n"  "concatenated list memory address : ",id(concatenated_list), "\n")  


copied_list = animal_names_list.copy()
print("copied list :",copied_list , "\n"  "copied list memory address : ",id(copied_list) , "\n")



#In-place modification of list does not create a new list and it modifies the original/existing list and 
#the memory address of the list remain unchanged

# Slice operations can do two things depending on how we use them:
# 1. Create a new list
# 2. Modify an existing list

# When we modify a list using slicing,
# Python replaces the elements in the specified index range.
# The old elements in that range are removed,
# and the new elements are inserted at that position
# in the original list.
# append and insert method also modify the original list and change the size of the list but not delete the original list it only add new element to the list and memory address of the list remain unchanged 

# When we print the result of append() , insert()  method it will return None because these methods modify the original list in-place and do not return a new list and because of that print statement return None

birds_list = ["sparrow", "eagle", "parrot", "crow", "pigeon"]
print("original birds_list memory address : ",id(birds_list) , "\n")


birds_list.append("peacock") #append "peacock" to the end of the list and modify the original list but memory address remain unchanged
print(id(birds_list) , "\n")

birds_list.insert(2,"peacock") #insert "peacock" at index 2 
print(id(birds_list) , "\n")

birds_list[2:5] = ["peacock", "owl", "hawk"]  
print(id(birds_list) , "\n")


# Loop through the list

for tea in tea_varities:
    print(tea)



#Removing element from the list
fruits_list = ["apple", "banana" , "orange" , "grapes" ,"kiwi", "blueberry", "blackberry","mango", "papaya", "watermelon"]
fruits_list.remove("orange")
print(fruits_list)




