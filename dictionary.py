# Dictionary :-  Changeable , Not allow duplicate ,  ordered , Use Key Value Pair , Written with curly braces{}

chai_types = {"Masala":"spicy" ,  "Ginger":"Zesty" ,  "Green":"Mild"}
print(chai_types)

#Access Specific Key
print(chai_types["Ginger"])


#Change Value 
#When we Change Value in Dictionary when we Modify existing value in dictionary then new object is not crated only existing object value is overright and deleted and new value place over there 


chai_types["Green"] = "Fresh"           # Assignment statement: updates the existing value and does not return anything
print(chai_types)


# Print dictionary using loops
#Important - : When we run Loop over a dictionary and think the variable will receieve both key and value from dictionary is wrong because Python is designed so that standard loop over a dictionary iterates over it's key means when we print direct loop variable wer receive only key in answer .

#If we need where loop access both key and value at a same time then we must explicitly use .item() method  
for chai in chai_types:
    print(chai_types[chai])                               #print(chai) only print Key 


#Using .item() method
for chai_data in chai_types.items():
    print(chai_data )


print()         # for space

for key , value in chai_types.items():
    print("new way : ", key,value)

#Check the length
print(len(chai_types))

#add a new key value in dictionary

chai_types["Earl Grey"] = "Citrus"
print(chai_types)