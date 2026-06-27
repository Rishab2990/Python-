userinput = int(input("Enter the number : "))
multiply = userinput *45
print(multiply)

# age classification
user_age = int(input("enter your age : "))

if user_age < 13:
    print("Child")
    
elif user_age < 20:
    print("Teenager")
    
elif user_age < 60:
    print("Adult")

elif user_age >= 60:
    print("Senior")

