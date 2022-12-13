class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("How many car are there?:")
        self.bal=input("How much bank balance are there?:")

class son(father):
    def printdata(self):
        print("Total Car:",self.car)
        print("Total Balance:",self.bal)

sn=son()
sn.getdata()
sn.printdata()