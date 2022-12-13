import re

unm=input("Enter your Username:")

unm_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(unm_pattern,unm)

if x:
    print("Username is valid!")
else:
    print("Error...Invalid Username.")