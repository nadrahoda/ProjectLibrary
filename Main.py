from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from subprocess import call
import Buttons as btns


def read_books():
    call(["python", "bookFile.py"])

def screenManipulation():
    red = Tk()
    red.title("Welcome to the online manager")
    red.geometry("1240x627+100+50")
    red.configure(bg="#d25d17")
    red.resizable(0, 0)

    my_text = Label(red, text="Welcome!",  font=('Goudy old style', 80, "bold"), fg="white", bg="#d25d17")
    my_text.place(x=100, y=50)
    my_text_two = Label(red, text="The J.N.N University sets the benchmarks of the global education\n \n"
                                  "with a system that matches the best of practices, \n\n theories, resources and "
                                  "standards\n\n all over the world."
                                  "J.N.N. aims to provide world class education, \n\nby incorporating advance technology\n\n"
                                  " into the curriculum to help learn better.",  font=('Open Sans', 15),
                        fg="lightgray", bg="#d25d17")
    my_text_two.place(x=60, y=200)
    my_text_three = Label(red, text="", font=('Goudy old style', 10, "bold"), fg="white", bg="#d25d17")
    my_text_three.place(x=100, y=250)

    btn1 = Button(red, text="Display the Register", font=('Goudy old style', 15, "bold"), width=25,
                  cursor="hand2", command=btns.btnAll_Click, activebackground="#d25d17")
    btn1.place(x=800, y=120)
    btn2 = Button(red, text="Issue and Return Books", font=('Goudy old style', 15, "bold"), width=25,
                  cursor="hand2", command=btns.btnIssue, activebackground="#d25d17")
    btn2.place(x=800, y=220)

    btn3 = Button(red, text="Books", font=('Goudy old style', 15, "bold"), width=25,
                  cursor="hand2", command=read_books, activebackground="#d25d17")
    btn3.place(x=800, y=320)
    btn4 = Button(red, text="Exit", font=('Goudy old style', 15, "bold"), width=25,
                  cursor="hand2", command=red.destroy, activebackground="#d25d17")
    btn4.place(x=800, y=420)
    screen.destroy()

class Login:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("The Online Library Manager")
        self.screen.geometry("1240x627+100+50")
        self.screen.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="library4.jpg")
        self.bg_Image = Label(self.screen, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame_login = Frame(self.screen, bg="white")
        frame_login.place(x=650, y=70, height=480, width=500)

        title = Label(frame_login, text="J.N.N. Scholar Library", font=('Impact', 30, "bold"), fg="#d77337",
                      bg="white").place(x=70, y=40)

        title2 = Label(frame_login, text="Member Login", font=('Goudy old style', 15, "bold"), fg="#d25d17",
                       bg="white").place(x=70, y=180)

        lbl1 = Label(frame_login, text="Enter Your Username", font=('Goudy old style', 12, "bold"), fg="gray",
                     bg="white").place(x=70, y=220)
        self.txt_user = Entry(frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=70, y=260, width=250, height=35)
        lbl2 = Label(frame_login, text="Enter Password", font=('Goudy old style', 12, "bold"), fg="gray",
                     bg="white").place(x=70, y=300)
        self.txt_pass = Entry(frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=70, y=340, width=250, height=35)

        btn = Button(frame_login, text="Login", bg="#d25d17", fg="white", font=("times new roman", 15),
                     command=self.login_function, cursor="hand2", activebackground="white", width=32).place(x=70, y=400)

    def login_function(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All the fields must be filled.", parent=self.screen)
        elif self.txt_user.get() != "abc" or self.txt_pass.get() != "111":
            messagebox.showerror("Error!", "Invalid Username or Password.", parent=self.screen)
        else:
            screenManipulation()

screen = Tk()
obj = Login(screen)
screen.mainloop()
