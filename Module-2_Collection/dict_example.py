mydict={'id':101,'name':'sanket','sub':'python'}

#print(mydict)
#print(mydict["name"])
#print(mydict.get("sub"))
#print(mydict.keys())
#print(mydict.values())

"""if 'name' in mydict:
    print('Yes...')
else:
    print('No')"""

"""if 'sanket' in mydict.values():
    print('Yes...')
else:
    print('No')"""

# ------------------------ #


"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

#Key=id and Value=101
#Key=name and Value=sanket

"""for i,j in mydict.items():
    #print(i)
    print(f"Key={i} and Value={j}")"""

# ---------------------------------------- #
print(mydict)
mydict["city"]="Rajkot"
#mydict.pop("sub")
#mydict.clear()
#del mydict
#print(mydict)

newdict=mydict.copy()
print(newdict)