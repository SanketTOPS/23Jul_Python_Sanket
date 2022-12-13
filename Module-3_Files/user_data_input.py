fl=open('new.txt','a')

n=int(input("Enter number of students info:"))

def getdata():
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stsub=input("Enter Subject:")

    fl.write(f"ID:{stid}\nName:{stnm}\nSubject:{stsub}\n")

for i in range(n):
    getdata()


