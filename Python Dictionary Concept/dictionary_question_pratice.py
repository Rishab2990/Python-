#Access value
student = {
    "name" : "rishab singh",
    "age" : 20,
    "city" : "delhi"
 }

print(student)  #print complete dictionary
print(" Student Name : ",student["name"])  # we use square brackets to access specific index value  
                                           # when we need to call any fuction/method then we use paranthesis

print("name")


#Update existing value  

student["age"] = 25  # INFO: Python never deletes integer values from -5 to 256. 
print(student)  # INFO : All values in this range are pre-allocated in the "Small Integer Cache" because they are frequently used. 
# INFO : When we switch from 20 to 25, Python doesn't create or delete anything; 
# INFO : it just moves the reference (pointer) from one cached number to another. Both numbers stay in memory.##



#Add new key-value pair

student["coutry"] = "India"
print(student)

#Delete Key 
#For deleting key we have few methods like del, pop() , popitem() , clear()
deleting_key =  student.pop("age") 
print("Deleted Key :", deleting_key )
print(student)


#Q5. Check Key Exists   "in" operator we can only use on single value not on complete dictionary .
#if we want to check both key and value we can use in operator with item() method
print("email" in student)
print(("name" , "age")  in student.items())

# Print only keys.  name , age , city
print(student.keys())




# Print: name -> Rishab     age -> 10000 , city -> Delhi     using .items()
print(student.items())

for key, value in student.items():
    print(key, "->" , value)



# Q9   Count total keys manually using loop.
print("Total Keys : ",len(student))  # INFO: len() function is used to count total keys in dictionary.


#  Count total keys manually using loop. without using len() function .

count = 0
for key in student:
    count +=1 
print("Total Keys manuall counting without using len() :  ",count)



#Adding new key value pair in dictionary

student["Occupation"] = "Machine Learning Engineer"
print(student)


# Q.   Find longest key.

for longest_key , longest_value in student.items():
    print(longest_key, longest_value)


# store_kye = 0
# for longest_keys in student():
#     store_key = longest_keys
#     if(len(longest_keys) > len(store_key)):
#         store_key = longest_keys
# print("Longest Key : " , store_key)

store_key = ""
for longest_keys in student.values():
    if(len(longest_keys) > len(store_key)):
        store_key = longest_keys
print("Longest key :",store_key)




# Q. Find highest score.
marks = {
    "Math":80,
    "Science":95,
    "English":70
}
highest_score = 0
for score in marks.values():
    if(score>highest_score):
        highest_score = score
print("Highest Score : ",highest_score)


#we can perform same operation with using 
print("Highest Score using max() function : ",max(marks.values()))  # INFO: max() function is used to find maximum value in dictionary.

# Another way in which we use extra variable in loop to find highest score.
Highest_score = 0 
Highest_subject = ""
for subject , Score in marks.items():
    if(Score > Highest_score):
        Highest_score = Score
        Highest_subject = subject
print("Highest Score using extra variable in loop : ",Highest_score , Highest_subject)


# Find average marks. 
total_number = 0
for score_marks in marks.values():
    total_number += score_marks
total_subjects = len(marks)
average_marks = total_number / total_subjects
print("Average Marks :" , average_marks)



