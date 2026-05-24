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
#Interesting thing about list how it affect memory when perform certain operations on it .

animal_names_list = ["cat", "dog", "rabbit", "hamster","tiger","lion"]
print("original list memory address : ",id(animal_names_list) , "\n")

slice_list = animal_names_list[2:5]  
print("slice list :  ",slice_list  )   
print("slice list memory address :",id(slice_list) ,  "\n\n")

concatenated_list = animal_names_list+["giraffe", "elephant"]
print("concatenated list :", concatenated_list,)  
print("concatenated list memory address ", id(concatenated_list), "\n")


print("copied list :",id(animal_names_list.copy()) , "\n\n") 

#check the memory address of the animal_names_list 
print("memory address :",id(animal_names_list))  # this will print the memory address of the animal_names_list