class student:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("This is getdata.")

# Object of Class
st=student()
print(st.stid)
print(st.stnm)
st.getdata()