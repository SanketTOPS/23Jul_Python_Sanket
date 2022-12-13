fl=open('stdata.txt','a')

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")

"""fl.write(stid)
fl.write(stnm)
fl.write(stsub)"""

fl.write(f"ID:{stid}\nName:{stnm}\nSubject:{stsub}\n")