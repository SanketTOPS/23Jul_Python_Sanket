class gfather:
    house=0
    gold=0

    def g_getdata(self):
        self.house=input("How many houses are there:")
        self.gold=input("How much gold are there:")

class father(gfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("How many car are there:")
        self.bal=input("How much bank balance are there:")

class son(father):
    def alldata(self):
        print("House:",self.house)
        print("Gold:",self.gold)
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.alldata()


