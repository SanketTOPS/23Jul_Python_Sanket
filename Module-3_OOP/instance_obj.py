class student:
    stid=12
    stnm='Sanket'

    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)


# Calling via Object
"""st=student()
st.printdata()
st.stid=45
st.stnm='Nirav'
st.printdata()"""

# Calling via Instance
student().printdata()
student().stid=34
student().stnm='Ashok'
student().printdata()  