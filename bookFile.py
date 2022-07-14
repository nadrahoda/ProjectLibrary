from tkinter import *
import webbrowser


orange = Tk()
orange.title("Read Books")
orange.geometry("1240x627+100+50")
orange.configure(bg="#d25d17")
orange.resizable(0, 0)



def data():
    Label(frame, text="SR.NO", font=('Goudy old style', 10, "bold"), relief="groove").grid(row=0, column=0, padx=10, pady=50)
    Label(frame, text="1", font=('Goudy old style', 15, "bold"), relief="groove").grid(row=1, column=0, pady=50)
    Label(frame, text="2", font=('Goudy old style', 15, "bold"), relief="groove").grid(row=2, column=0, pady=50)
    Label(frame, text="3", font=('Goudy old style', 15, "bold"), relief="groove").grid(row=3, column=0, pady=50)
    Label(frame, text="4", font=('Goudy old style', 15, "bold"), relief="groove").grid(row=4, column=0, pady=50)

    Label(frame, text="BOOK TITLE", font=('Goudy old style', 10, "bold"), relief="groove").grid(row=0, column=1)
    Label(frame, text="Migration, Gender \nand Social Justice \n (Perspectives on Human Insecurity)",
          font=('Goudy old style', 15, "bold")).grid(row=1, column=1)
    Label(frame, text="The Illusion of Risk Control",  font=('Goudy old style', 15, "bold")).grid(row=2, column=1)
    Label(frame, text="Knowledge Solutions",  font=('Goudy old style', 15, "bold")).grid(row=3, column=1)
    Label(frame, text="The Great Mindshift",  font=('Goudy old style', 15, "bold"), borderwidth=0).grid(row=4, column=1)

    Label(frame, text="AUTHOR", font=('Goudy old style', 10, "bold"), relief="groove").grid(row=0, column=2)
    Label(frame, text="Thanh-Dam \n Truong", font=('Goudy old style', 12, "bold")).grid(row=1, column=2)
    Label(frame, text="Gilles Motet, \nCorinne Bieder", font=('Goudy old style', 12, "bold")).grid(row=2, column=2)
    Label(frame, text="Oliver Serrat", font=('Goudy old style', 12, "bold")).grid(row=3, column=2)
    Label(frame, text="Maja Gopel", font=('Goudy old style', 12, "bold")).grid(row=4, column=2)

    Label(frame, text="READ", font=('Goudy old style', 10, "bold"), relief="groove").grid(row=0, column=3)

    link = Label(frame, wraplength=200, justify="center", relief="sunken",  font=('Goudy old style', 12, "bold"),
                 text="https://link.springer.com/content/pdf/10.1007%2F978-3-642-28012-2.pdf",
                 fg="blue", cursor="hand2")
    link.grid(row=1, column=3, padx=40)
    link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))

    link = Label(frame, wraplength=200, justify="center", relief="sunken",  font=('Goudy old style', 12, "bold"),
                 text="https://link.springer.com//content/pdf/10.1007%2F978-3-319-32939-0.pdf",
                 fg="blue", cursor="hand2")
    link.grid(row=2, column=3)
    link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))

    link = Label(frame, wraplength=200, justify="center", relief="sunken",  font=('Goudy old style', 12, "bold"),
                 text="https://link.springer.com/book/10.1007/978-981-10-0983-9",
                 fg="blue", cursor="hand2")
    link.grid(row=3, column=3)
    link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))

    link = Label(frame, wraplength=200, justify="center", relief="sunken",  font=('Goudy old style', 12, "bold"),
                 text="https://link.springer.com//content/pdf/10.1007%2F978-3-319-43766-8.pdf",
                 fg="blue", cursor="hand2")
    link.grid(row=4, column=3)
    link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))



##################################################################################################



def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=800, height=450)


myframe = Frame(orange, relief=GROOVE, width=10, height=10, bd=1)
myframe.place(x=200, y=90)

canvas = Canvas(myframe)
frame = Frame(canvas)

myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)
data()

btnforback = Button(orange, text="exit", command=orange.destroy, font=('Goudy old style', 15, "bold"), width=10,
                    cursor="hand2", activebackground="#d25d17")
btnforback.place(x=1080, y=560)
my_tex = Label(orange, text="Read Books (Download PDFs and enjoy!)", font=('Goudy old style', 20, "bold"), fg="white",
               bg="#d25d17")
my_tex.place(x=40, y=30)


##############################################################################################

orange.mainloop()
