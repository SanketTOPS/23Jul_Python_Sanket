fl=open("new.txt","r+")

print(fl.read())
#print(fl.readline())
#print(fl.readlines()[6:9])

"""if fl.readable():
    print("Yes...")
else:
    print("Error!")"""

"""for i in fl:
    print(i)
"""

fl.write("\nHello")