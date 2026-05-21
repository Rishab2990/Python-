# a list is built-in data structure in python that is used to store collection of items. It is a mutable/changeable , allow duplicate
# and ordered collection of items. we use square brackets[] to define a list 

tea_varities = ["green tea", "black tea", "oolong tea", "white tea", "herbal tea"]
print(tea_varities) #after printing statement python immediately delete the list from memory because we have not assigned a variable 

#print specfic element from the list
print(tea_varities[2])

print(tea_varities[1:2])

# new_tea = tea_varities[1:2]= ["chamomile tea"] # this code will replace the element at index 1 with "chamomile tea" and assign the new list to variable new_tea
# print(new_tea)

print(tea_varities[1:2],"chamomile tea") # this code will replace the element at index 1 with "chamomile tea" and assign the new list to variable new_tea but in this code we are not assigning the new list to any variable so after printing statement python immediately delete the new list from memory because we have not assigned a variable to it.