import tkinter
import os
from tkinter import messagebox
from tkinter.ttk import Combobox
window=tkinter.Tk()

window.title("FirstApp")
window.geometry("500x600")
window.config(background="gold")

#tkinter.Label(text="Firstname:").pack()
#tkinter.Label(text="Lastname:").pack()

#tkinter.Label(text="Firstname:").place(x=0,y=0)
#tkinter.Label(text="Lastname:").place(x=0,y=30)


tkinter.Label(text="Firstname:",bg='gold',font='Garamond 15 bold',fg='red').grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='gold',font='Garamond 15 bold',fg='red').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text='Male',bg='gold',font='Garamond 15 bold',fg='red').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text='Female',bg='gold',font='Garamond 15 bold',fg='red').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text="Python",bg='gold',font='Garamond 15 bold',fg='red').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text="JAVA",bg='gold',font='Garamond 15 bold',fg='red').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text="iOS",bg='gold',font='Garamond 15 bold',fg='red').grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text="PHP",bg='gold',font='Garamond 15 bold',fg='red').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar']
Combobox(values=city).grid(row=7,column=0)

def btnclick():
    #print("This is Tkinter")
    #messagebox.showerror("Error","Somthing went wrong...")
    #messagebox.showwarning("Warning!","Your disk is full.")
    #messagebox.showinfo("Success","Login Success!")
    #os.startfile("chrome")
    os.system("calc")


tkinter.Button(text="Submit",font='Garamond 15 bold',command=btnclick).place(x=200,y=300)

tkinter.mainloop()
