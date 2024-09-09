import tkinter as t
from PIL import Image, ImageTk
import connection
global con,mycursor
from tkinter import messagebox
import superadmin as s
import admin as a
import os
import students as r

con,mycursor=connection.myconnections()
os.chdir("C:\\Users\\Shubham Kapoor\\Desktop\\qwe")
def dologin(ue,pw,root):
    query="select * from user_table where email = '%s'"%(ue)
    mycursor.execute(query)
    data=mycursor.fetchall()
    if(len(data)>0):
        dp=data[0][0]
        if(dp==pw):
            roleid=data[0][7]
            if roleid==1:
                root.destroy()



                s.superadminscreen()
            elif roleid==2:
                root.destroy()
                a.adminscreen()
            elif roleid==3:
                root.destroy()
                r.studentscreen()
        else:
            messagebox.showinfo("Password Error","Wrong Password")
    else:
        messagebox.showinfo("Login Error","Wrong Email")
def loginscreen():
    root=t.Tk()

    image = Image.open("libook.jpg")
    background_image = ImageTk.PhotoImage(image)
    background = t.Label(image=background_image)
    background.pack(fill=t.BOTH, expand=t.YES)
#---------------------------------------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------
    #code for gif
    '''frames = [ImageTk.PhotoImage(file='images/backimage.gif',format = 'gif -index %i' %(i)) for i in range(100)]
    background = t.Label(root)
    background.pack(fill=t.BOTH, expand=t.YES)
    def update(ind):

        frame = frames[ind]
        ind += 1
        background.configure(image=frame)
        root.after(100, update, ind)'''
    #end code for gif
    root.title("login window")
    root.geometry("1000x600")
    root.config(bg="green")

    label1=t.Label(background,fg="white",bg="brown",text="UserEmail")
    label1.grid(row=0,column=0,padx=10,pady=10)
    textbox1=t.Entry(background)
    textbox1.grid(row=0,column=1)

    label2=t.Label(background,fg="white",bg="brown",text="UserPassword")
    label2.grid(row=1,column=0)
    textbox2=t.Entry(background,show="*")
    textbox2.grid(row=1,column=1)

    button1=t.Button(background,text="Login",width=15,height=2,bg="black",fg="white",command=lambda :dologin(textbox1.get(),textbox2.get(),root))
    button1.grid(row=2,column=1,pady=10)
    root.resizable(0,0)
    #root.after(0, update, 0)
    root.mainloop()


#loginscreen()
