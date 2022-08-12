from cgitb import text
from sys import dont_write_bytecode
from tkinter import *
from turtle import back, window_width
from PIL import ImageTk , Image

class loginForm : 
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        # self.window.state('zoomed')

        # ========= background =========
        self.bg_frame = Image.open('images\\login_bg.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window,image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both' , expand='yes')

        # ========= signup frame =========
        self.lg_frame = Frame(self.window , bg = 'grey' , width=650 , height=550)
        self.lg_frame.place(x=258,y=100)

        # ========= heading =========
        self.heading = Label(self.lg_frame, text='SIGN UP' , font=25 , bg='grey') 
        self.heading.place(x=8 , y=30 , width=634 , height=30)

        # ========= institution name =========
        self.institution_label = Label(self.lg_frame , text='Institution name : ' , bg='grey' , font=(30))
        self.institution_label.place(x=250 , y= 100 , width=150 , height=20)   

        self.email_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , highlightthickness=0)
        self.email_textbox.place(x=200 , y=130 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.email_line.place(x=200 , y=150)

        # ========= email =========
        self.email_label = Label(self.lg_frame , text='email : ' , bg='grey' , font=(30))
        self.email_label.place(x=250 , y= 180 , width=150 , height=20)   

        self.email_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , highlightthickness=0)
        self.email_textbox.place(x=200 , y=210 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.email_line.place(x=200 , y=230)

        # ========= password =========
        self.password_label = Label(self.lg_frame , text='password : ' , bg='grey' , font=(30))
        self.password_label.place(x=250 , y= 260 , width=150 , height=20)   

        self.password_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , show='*')
        self.password_textbox.place(x=200 , y=290 , width=250 , height=20)

        self.password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.password_line.place(x=200 , y=310)

        # ========= confirm password =========
        self.confirm_password_label = Label(self.lg_frame , text=' confirm password : ' , bg='grey' , font=(30))
        self.confirm_password_label.place(x=250 , y= 340 , width=150 , height=20)   

        self.confirm_password_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , show='*')
        self.confirm_password_textbox.place(x=200 , y=370 , width=250 , height=20)

        self.confirm_password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.confirm_password_line.place(x=200 , y=390)

        # ========= sign up button =========
        self.login_button = Image.open('images\\login_button.png')
        login_button_photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.lg_frame , image= login_button_photo , bg='grey')
        self.login_button_label.image = login_button_photo
        self.login_button_label.place(x=200 , y=420 , width=250 , height=50)

        self.login = Button(self.login_button_label , text='register' , font=(25) , bd=0 , cursor='hand2' , activeforeground='grey' , activebackground= '#1995CC', fg='black' , background='#1995CC' , command=validateAccount)
        self.login.place(x=55,y=10 ,width=130 )


def page():
    window = Tk()
    loginForm(window)
    window.mainloop()

def validateAccount():
    print('login is pressed')

page()
