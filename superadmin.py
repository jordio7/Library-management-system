import tkinter as t


def addbooks():
    root1=t.Tk()
    root1.title("Add Books Screen")
    root1.geometry("1600x800")
    root1.config(bg="#2C81C4")
    bookname=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Book Name")
    bookname.grid(row=0,column=0,padx=50,pady=20)
    bookentry=t.Entry(root1,width=20)
    bookentry.grid(row=0,column=1)

    quantity=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Quantity")
    quantity.grid(row=1,column=0)
    quantityentry=t.Entry(root1,width=20)
    quantityentry.grid(row=1,column=1)

    author=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Author")
    author.grid(row=2,column=0,pady=20)
    authorentry=t.Entry(root1,width=20)
    authorentry.grid(row=2,column=1)

    barcode=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Scan Barcode")
    barcode.grid(row=3,column=0,pady=20)
    barcodebutton=t.Button(root1,width=20,text="Scan")
    barcodebutton.grid(row=3,column=1)


    is_active=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Is_active")
    is_active.grid(row=4,column=0)
    is_activeentry=t.Entry(root1,width=20)
    is_activeentry.grid(row=4,column=1)

    is_issued=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Is_issued")
    is_issued.grid(row=5,column=0)
    is_issuedentry=t.Entry(root1,width=20)
    is_issuedentry.grid(row=5,column=1)

    registered_date=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Registered_date")
    registered_date.grid(row=6,column=0)
    registered_dateentry=t.Entry(root1,width=20)
    registered_dateentry.grid(row=6,column=1)




    image=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Image")
    image.grid(row=7,column=0)
    imagebutton=t.Button(root1,width=20,text="Upload Image")
    imagebutton.grid(row=7,column=1)



    addbutton=t.Button(root1,width=20,text="Add Book")
    addbutton.grid(row=8,column=1)






    #viewbook
def viewbooks():
    root1=t.Tk()
    root1.title("View Books Screen")
    root1.geometry("500x500")
    root1.config(bg="#2C81C4")
    bookname=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Book Name")
    bookname.grid(row=0,column=0,padx=50,pady=20)
    bookentry=t.Entry(root1,width=20)
    bookentry.grid(row=0,column=1)
    quantity=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Quantity")
    quantity.grid(row=1,column=0)
    quantityentry=t.Entry(root1,width=20)
    quantityentry.grid(row=1,column=1)
    author=t.Label(root1,fg="#FFFFFF",bg="#2C81C4",text="Author")
    author.grid(row=2,column=0,pady=20)
    authorentry=t.Entry(root1,width=20)
    authorentry.grid(row=2,column=1)

    addbutton=t.Button(root1,width=20,text="View Book")
    addbutton.grid(row=6,column=1)

    root1.resizable(0,0)
    root1.mainloop()







def superadminscreen():
    root=t.Tk()
    root.title("Super Admin Screen"
               "                                                                                                                                                              University Institue of Information Technology")


    root.config(bg="turquoise")


    #menubar
    menuobj = t.Menu(root,tearoff=0)
    root.config(menu = menuobj)
    filemenu = t.Menu(menuobj)
    menuobj.add_cascade(label="Books", menu=filemenu)
    filemenu.add_command(label="AddNew",
                    accelerator="Ctrl+N",
                         command=lambda :addbooks())

    menuobj.add_cascade(label="View", menu=filemenu)
    filemenu.add_command(label="viewbook",
                    accelerator="Ctrl+K",
                         command=lambda :viewbooks())






    menuobj.add_cascade(label="BarCode", menu=filemenu)
    filemenu.add_command(label="Scan",
                    accelerator="Ctrl+S",
                         command=lambda :addbooks())






    root.state("zoomed")
    root.mainloop()
#superadminscreen()
#addbooks()
