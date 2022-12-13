class student:
    __stid=2
    __stnm='Ashok'

    def getdata(self):
        print("This is getdata.")
    
    def __printdata(self):
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)
    
    def alldata(self):
        self.__printdata()

st=student()
#print(st.stid)
#print(st.stnm)
st.getdata()
#st.printdata()
st.alldata()