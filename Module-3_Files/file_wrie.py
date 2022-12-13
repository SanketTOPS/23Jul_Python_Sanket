fl=open('test.txt','w')
fl.write("This is Python!")

if fl.writable():
    print("Yes...")
else:
    print("Error!")
