
#Access value

student = {
    "name" : "rishab singh",
    "age" : 20,
    "city" : "delhi"
 }

print(student)  #print complete dictionary
print(" Student Name : ",student["name"])  # we use square brackets to access specific index value  
                                           # when we need to call any fuction/method then we use paranthesis


#Update existing value  
student["age"] = 25  # INFO: Python never deletes integer values from -5 to 256. 
print(student)  # INFO : All values in this range are pre-allocated in the "Small Integer Cache" because they are frequently used. 
# INFO : When we switch from 20 to 25, Python doesn't create or delete anything; 
# INFO : it just moves the reference (pointer) from one cached number to another. Both numbers stay in memory.##


