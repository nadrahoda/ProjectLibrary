from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Functions as func


def btnIssue():
    global varName
    global varId
    global varStream
    global varDate
    global varBook


    def issue_Click():
        if varName.get()=="" or varID.get()=="" or varStream.get()=="" or varDate.get() =="" or varBook.get() ==""  :
            messagebox.showerror("The Online Library Manager", "All the fields are required.")
        else:
            borrow = func.Issue()
            borrow.bookIssue()
            borrow.name = varName.get()
            borrow.id = varID.get()
            borrow.stream = varStream.get()
            borrow.date = varDate.get()
            borrow.book = varBook.get()
            messagebox.showinfo("Issue A Book ", f"Book '{borrow.book}' issued successfully to {borrow.name}.")
            varName.set("")
            varID.set("")
            varStream.set("")
            varDate.set("")
            varBook.set("")

    def btnReturn_Click():
        ques = messagebox.askyesno("Before you proceed",
                                   "Do you want to return a book?")
        if ques == True:
            borrow = func.Issue()
            borrow.book = varBook.get()
            res = borrow.returnBook()
            if res == 1:
                messagebox.showinfo("The Online Library Manager", f"Book '{borrow.book}' Returned Successfully By {borrow.name}")
            else:
                messagebox.showerror("The Online Library Manager", "No such records exist")

    issueW = Tk()
    issueW.title("Issue/Return a Book")
    issueW.geometry("1240x627+100+50")
    issueW.configure(bg="white")
    issueW.resizable(0, 0)
    issueW.update()
    title_issue = Label(issueW, text="Amity Scholar Library", font=('Impact', 30, "bold"), fg="#d77337",
                        bg="white").place(x=130, y=30)

    titleSub = Label(issueW, text="Kindly fill out this form and submit!"
                                  , font=('Goudy old style', 15, "bold"),
                     fg="#d25d17", bg="white").place(x=70, y=120)

    btnExit = Button(issueW, text="Exit", bg="#d77337", fg="black", font=("times new roman", 15),
                     activebackground="#d25d17", width=10, command=issueW.destroy).place(x=1040, y=550)
    image = Image.open("kids.gif")
    resize_image = image.resize((420, 420))
    img = ImageTk.PhotoImage(resize_image)
    label1 = Label(issueW, image=img)
    label1.image = img
    label1.place(x=730, y=80)

    lblBook = Label(issueW, text="Book Number: ", bg="white", fg="gray",
                    font=('Goudy old style', 15, "bold"))
    lblBook.place(x=70, y=160)

    varBook = StringVar()
    entryBook = Entry(issueW, textvariable=varBook, font=("Times New Roman", 20), bg="lightgray")
    entryBook.place(x=300, y=160)

    lblName = Label(issueW, text="Name of the Student: ", bg="white", fg="gray",
                    font=('Goudy old style', 15, "bold"))
    lblName.place(x=70, y=200)

    varName = StringVar()
    entryName = Entry(issueW, textvariable=varName, font=("Times New Roman", 20), bg="lightgray")
    entryName.place(x=300, y=200)

    lblID = Label(issueW, text="Student ID Number: ", bg="white", fg="gray", font=('Goudy old style', 15, "bold"))
    lblID.place(x=70, y=240)

    varID = StringVar()
    entryID = Entry(issueW, textvariable=varID, font=("Times New Roman", 20), bg="lightgray")
    entryID.place(x=300, y=240)

    lblStream = Label(issueW, text="Stream: ", bg="white", fg="gray", font=('Goudy old style', 15, "bold"))
    lblStream.place(x=70, y=280)

    varStream = StringVar()
    entryStream = Entry(issueW, textvariable=varStream, font=("Times New Roman", 20), bg="lightgray")
    entryStream.place(x=300, y=280)

    lblDate = Label(issueW, text="Date of Book Issue: ", bg="white", fg="gray",
                    font=('Goudy old style', 15, "bold"))
    lblDate.place(x=70, y=320)
    varDate = StringVar()
    entryDate = Entry(issueW, textvariable=varDate, font=("Times New Roman", 20), bg="lightgray")
    entryDate.place(x=300, y=320)



    btn = Button(issueW, text="Return Book", font=("times new roman", 15), width=46,
                  cursor="hand2", command=btnReturn_Click, activebackground="#d25d17")
    btn.place(x=70, y=450)

    btn1 = Button(issueW, text="Issue Book", bg="#d25d17", fg="white", font=("times new roman", 15),
                 cursor="hand2", command=issue_Click, activebackground="white", width=46).place(x=70, y=400)
    titleInfo = Label(issueW, text="(To return, please enter the book no. and click on 'Return Book')",
                      font=('times new roman', 15), fg="gray", bg="white").place(x=70, y=500)


def btnAll_Click():
    root1 = Tk()
    root1.title("Records")
    root1.configure(bg="white")
    root1.geometry("1200x500+150+150")
    root1.resizable(0, 0)
    lblname1 = Label(root1, text="Name", fg="#d77337", bg="white", width=10, font=("Times New Roman", 20, "bold"))
    lblname1.grid(row=0, column=0, padx=14, pady=10)
    lblid = Label(root1, text="ID", fg="#d77337", bg="white", width=10, font=("Times New Roman", 20, "bold"))
    lblid.grid(row=0, column=1, padx=14)
    lblstream = Label(root1, text="Stream", fg="#d77337", bg="white", width=10,
                      font=("Times New Roman", 20, "bold"))
    lblstream.grid(row=0, column=2, padx=14)
    lbldate = Label(root1, text="Date", fg="#d77337", bg="white", width=10, font=("Times New Roman", 20, "bold"))
    lbldate.grid(row=0, column=3, padx=14)
    lblbook = Label(root1, text="Book Number", fg="#d77337", bg="white", width=10, font=("Times New Roman", 20, "bold"))
    lblbook.grid(row=0, column=4, padx=14)
    lblstatus = Label(root1, text="Book Status", fg="#d77337", bg="white", width=10, font=("Times New Roman", 20, "bold"))
    lblstatus.grid(row=0, column=5, padx=14)

    i = 1
    for borrow in func.Issue.list_one:
        lblForName = Label(root1, text=f"{borrow.name}", fg="black", bg="white", width=10,
                           font=("Times New Roman", 15))
        lblForName.grid(row=i, column=0)
        lblForId = Label(root1, text=f"{borrow.id}", fg="black", bg="white", width=10,
                         font=("Times New Roman", 15))
        lblForId.grid(row=i, column=1)
        lblForStream = Label(root1, text=f"{borrow.stream}", fg="black", bg="white", width=10,
                             font=("Times New Roman", 15))
        lblForStream.grid(row=i, column=2)
        lblForDate = Label(root1, text=f"{borrow.date}", fg="black", bg="white", width=10,
                           font=("Times New Roman", 15))
        lblForDate.grid(row=i, column=3)
        lblForBook = Label(root1, text=f"{borrow.book}", fg="black", bg="#d77337", width=10,
                           font=("Times New Roman", 15))
        lblForBook.grid(row=i, column=4)
        lblForStatus = Label(root1, text=f"{borrow.status}", fg="black", bg="white", width=10,
                           font=("Times New Roman", 15))
        lblForStatus.grid(row=i, column=5)

        i += 1

    btn3 = Button(root1, text="Exit", bg="#d25d17", fg="white", font=("times new roman", 15),
                 cursor="hand2", command=root1.destroy, activebackground="white", width=10).place(x=1000, y=450)
