import re

mystr="This is Python!"

x=re.search("Python",mystr)

print(x)
if x:
    print("Valid...")
else:
    print("Error...Not valid!")