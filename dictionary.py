# Dictionary :-  Changeable , Not allow duplicate ,  ordered , Use Key Value Pair , Written with curly braces{}

chai_types = {"Masala":"spicy" ,  "Ginger":"Zesty" ,  "Green":"Mild"}
print(chai_types)

#Access Specific Key
print(chai_types["Ginger"])


#Change Value 
#When we Change Value in Dictionary when we Modify existing value in dictionary then new object is not crated only existing object value is overright and deleted and new value place over there 


chai_types["Green"] = "Fresh"           # Assignment statement: updates the existing value and does not return anything
print(chai_types)


#Print dictionary using loops
for chai in chai_types:
    print(chai)