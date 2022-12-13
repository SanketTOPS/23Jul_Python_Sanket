class student:
    def getdata(self,id,name):
        print("Student ID:",id)
        print("Student Name:",name)


class otherstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)

ot=otherstudent()
ot.getdata(1,'Sanket')

st=student()
st.getdata(12,'Nirav')