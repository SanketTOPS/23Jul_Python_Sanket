tech=["Python","IOS","Android","JAVA","PHP"]

"""print(tech)
print(tech[0]) 
print(tech[-1])
print(tech[0:3]) #slicing
print(tech[0:])
print(tech[:3])"""

#print(len(tech))

"""if "Python" in tech:
    print("Yes...")
else:
    print("Noo..")"""

#print(tech)
#tech[1]="SWIFT"
#print(tech)

#Index[0]=Python
#Index[1]=IOS

#print(tech.index("JAVA"))

"""for i in tech:
    #print(i)
    print(f"Index[{tech.index(i)}]={i}")"""

# ----------------------------------------- #

print(tech)

tech.append("React")
tech.insert(2,"Node")
#tech.remove("JAVA")
#tech.pop()
#tech.pop(2)
#tech.clear()
#del tech[1]
#del tech
#tech.sort()
#tech.reverse()
#print(tech)

#newlist=tech.copy()

newlist=["C","C++","DS","CG"]
print(newlist)
#print(tech+newlist)
tech.extend(newlist)
print(tech)