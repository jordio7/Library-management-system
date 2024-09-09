import tkinter as t
from PIL import Image, ImageTk
from tkinter import messagebox
import os
os.chdir("C:\\Users\\Shubham Kapoor\\Desktop\\qwe")

def adminscreen():
    '''v=t.IntVar()'''
    root=t.Tk()
    root.title("Admin Screen")
    root.geometry("500x312")
    '''root.config(bg="#2C81C4")'''

    image = Image.open("libook.jpg")
    background_image = ImageTk.PhotoImage(image)
    background = t.Label(image=background_image)
    background.pack(fill=t.BOTH, expand=t.YES)


    label1=t.Label(background,fg="white",bg="brown",text="Admin")
    label1.grid(row=0,column=0,padx=10,pady=10)
    textbox1=t.Entry(background)
    textbox1.grid(row=0,column=1)

    label2=t.Label(background,fg="white",bg="brown",text="Add New Adimn")
    label2.grid(row=1,column=0)
    textbox2=t.Entry(background)
    textbox2.grid(row=1,column=1)

    button1=t.Button(background,text="Add",width=15,height=2,bg="black",fg="white")
    button1.grid(row=5,column=1,pady=10)

    root.resizable(0,0)
    root.mainloop()

#adminscreen
