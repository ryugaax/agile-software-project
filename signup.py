from tkinter import *
from tkinter import messagebox
from turtle import back, window_width
from PIL import ImageTk , Image
import csv
import re
import os
import login

class signupForm : 
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        institution_name = StringVar()
        user_email = StringVar()
        user_password = StringVar()
        user_confirm_password = StringVar()
        # self.window.state('zoomed')

        # ========= background =========
        self.bg_frame = Image.open('images\\login_bg.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window,image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both' , expand='yes')

        # ========= signup frame =========
        self.lg_frame = Frame(self.window , bg = 'black' , width=650 , height=550)
        self.lg_frame.place(x=258,y=100)

        # ========= heading =========
        self.heading = Label(self.lg_frame, text='SIGN UP' , font=25 , bg='black' , fg='white') 
        self.heading.place(x=8 , y=30 , width=634 , height=30)

        # =========back button===========
        self.back_button_photo = Image.open('images\\back.png')
        back_image=ImageTk.PhotoImage(self.back_button_photo)
        self.back_button = Button(self.lg_frame , image=back_image ,cursor="hand2" , background="black" , relief=FLAT , command=self.loadLoginPage)
        self.back_button.image = back_image
        self.back_button.place(x=8 , y=10 ,width=50,height=50)

        # ========= institution name =========
        self.institution_label = Label(self.lg_frame , text='Institution name : ' , bg='black' , font=(30) , fg='white')
        self.institution_label.place(x=250 , y= 100 , width=150 , height=20)   

        self.insti_textbox = Entry(self.lg_frame , font=(25) , bg='black' , relief='flat' , highlightthickness=0 , textvariable=institution_name , fg='white' , insertbackground='white')
        self.insti_textbox.place(x=200 , y=130 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.email_line.place(x=200 , y=150)

        # ========= email =========
        self.email_label = Label(self.lg_frame , text='email : ' , bg='black' , fg='white' , font=(30))
        self.email_label.place(x=250 , y= 180 , width=150 , height=20)   

        self.email_textbox = Entry(self.lg_frame , font=(25) , bg='black' , relief='flat' , highlightthickness=0 , textvariable=user_email , insertbackground='white' , fg='white')
        self.email_textbox.place(x=200 , y=210 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.email_line.place(x=200 , y=230)

        # ========= password =========
        self.password_label = Label(self.lg_frame , text='password : ' , bg='black' , fg='white' , font=(30))
        self.password_label.place(x=250 , y= 260 , width=150 , height=20)   

        self.password_textbox = Entry(self.lg_frame , font=(25) , bg='black' , relief='flat' , show='*' , textvariable=user_password , fg='white' , insertbackground='white')
        self.password_textbox.place(x=200 , y=290 , width=250 , height=20)

        self.password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.password_line.place(x=200 , y=310)

        # ========= confirm password =========
        self.confirm_password_label = Label(self.lg_frame , text=' confirm password : ' , bg='black' , font=(30) , fg='white')
        self.confirm_password_label.place(x=250 , y= 340 , width=150 , height=20)   

        self.confirm_password_textbox = Entry(self.lg_frame , font=(25) , bg='black' , fg='white',insertbackground='white' , relief='flat' , show='*' , textvariable=user_confirm_password)
        self.confirm_password_textbox.place(x=200 , y=370 , width=250 , height=20)

        self.confirm_password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.confirm_password_line.place(x=200 , y=390)

        # ========= sign up button =========
        self.signup_button = Image.open('images\\login_button.png')
        signup_button_photo = ImageTk.PhotoImage(self.signup_button)
        self.signup_button_label = Label(self.lg_frame , image= signup_button_photo , bg='black')
        self.signup_button_label.image = signup_button_photo
        self.signup_button_label.place(x=200 , y=420 , width=250 , height=50)

        self.signup = Button(self.signup_button_label , text='register' , font=(25) , bd=0 , cursor='hand2' , activeforeground='grey' , activebackground= '#1995CC', fg='black' , background='#1995CC' , command= lambda : self.validateAccount(self.email_textbox , self.password_textbox , self.confirm_password_textbox , self.insti_textbox))
        self.signup.place(x=55,y=10 ,width=130 , height=30 )


    def signupPage(self):
        self.window.mainloop()

    def validateAccount(self,email_entry , password_entry , confirm_entry , institution_entry):
        user_email = email_entry.get()
        user_password = password_entry.get()
        confirm_password = confirm_entry.get()
        institution_name = institution_entry.get()
        email_to_match = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

        if user_password == '' or user_email == '' or institution_name =='':
             messagebox.showerror(title="Error" , message="Please fill in the required entries")
             return
        else:
            if(user_password!=confirm_password):
                messagebox.showerror(title="Error" , message="Password is not correct")
                return
        
            if os.path.exists('users_account.csv'):
                with open('users_account.csv', encoding='UTF8' , newline='') as f:
                 for row in f:
                      if row.split(',')[1] == user_email:
                          messagebox.showerror(title="Error" , message="Email has already been registered")
                          return

            if re.match(email_to_match,user_email):
                self.registerAccount(user_email , user_password , institution_name)
                messagebox.showinfo(message="Account has been registered")
            else:
                messagebox.showerror(title="Error" , message="Email is invalid")
                return

        email_entry.delete(0 ,  END)
        password_entry.delete(0 , END)
        confirm_entry.delete(0 , END)
        institution_entry.delete(0 , END)
        
    def registerAccount(self , user_email , user_password , institution_name):
        # header = ['institution_name' , 'user_email' , 'user_password' ]
        data = [institution_name ,user_email , user_password]
        with open('users_account.csv', 'a', encoding='UTF8' , newline='') as f:
            writer = csv.writer(f)
        # write the data
            writer.writerow(data)

    def loadLoginPage(self):
        loginPage = login.loginForm(self.window)
        loginPage.loginPage()

# https://www.simplifiedpython.net/python-gui-login/