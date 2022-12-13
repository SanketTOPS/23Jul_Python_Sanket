import re

password=input("Enter Password:")
#cpassword=input("Enter Confirm Password:")

password_pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"

x=re.findall(password_pattern,password)

if x:
    print("Password is valid!")
else:
    print("Invalid Password....Try again!")
