import tkinter as t
from PIL import Image, ImageTk
from tkinter import messagebox
import os
os.chdir("C:\\Users\\SHUBHAM KAPOOR\\Desktop\\qwe")

def studentscreen():
    '''v=t.IntVar()'''
    root=t.Tk()
    root.title("Student Screen")
    root.geometry("1024x696")
    '''root.config(bg="#2C81C4")'''

    image = Image.open("libook.jpg")
    background_image = ImageTk.PhotoImage(image)
    background = t.Label(image=background_image)
    background.pack(fill=t.BOTH, expand=t.YES)


    label1=t.Label(background,fg="white",bg="brown",text="Name")
    label1.grid(row=0,column=0,padx=10,pady=10)
    textbox1=t.Entry(background)
    textbox1.grid(row=0,column=1)

    label2=t.Label(background,fg="white",bg="brown",text="Father's Name")
    label2.grid(row=1,column=0)
    textbox2=t.Entry(background)
    textbox2.grid(row=1,column=1)

    label3=t.Label(background,fg="white",bg="brown",text="University Roll No.")
    label3.grid(row=2,column=0)
    textbox3=t.Entry(background)
    textbox3.grid(row=2,column=1)

    label4=t.Label(background,fg="white",bg="brown",text="Address")
    label4.grid(row=3,column=0)
    textbox4=t.Entry(background)
    textbox4.grid(row=3,column=1)

    label5=t.Label(background,fg="white",bg="brown",text="Email")
    label5.grid(row=4,column=0)
    textbox5=t.Entry(background)
    textbox5.grid(row=4,column=1)

    label6=t.Label(background,fg="white",bg="brown",text="Password")
    label6.grid(row=5,column=0)
    textbox6=t.Entry(background)
    textbox6.grid(row=5,column=1)

    label7=t.Label(background,fg="white",bg="brown",text="Mobile No.")
    label7.grid(row=6,column=0)
    textbox7=t.Entry(background)
    textbox7.grid(row=6,column=1)

    label8=t.Label(background,fg="white",bg="brown",text="DOB")
    label8.grid(row=7,column=0)
    textbox8=t.Entry(background)
    textbox8.grid(row=7,column=1)

    button1=t.Button(background,text="Add",width=15,height=2,bg="black",fg="white")
    button1.grid(row=8,column=1,pady=10)

    root.resizable(0,0)
    #root.state("zoomed")
    root.mainloop()

#studentscreen
