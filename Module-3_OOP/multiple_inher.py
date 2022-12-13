class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class mitesh:
    mid=0
    msub=''

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.msub=input("Enter Mitesh's Subject:")

class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class tops(nirav,mitesh,ashok):
    def alldata(self):
        print("----------Nirav----------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("----------Mitesh----------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Subject:",self.msub)
        print("----------Ashok----------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)

tp=tops()
tp.n_getdata()
tp.m_getdata()
tp.a_getdata()
tp.alldata()

