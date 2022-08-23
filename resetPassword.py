from asyncore import read, write
from cgitb import text
import email
from email import header
from linecache import getline
import logging
from sys import dont_write_bytecode
from tkinter import *
from tokenize import String
from turtle import back, window_width
from PIL import ImageTk , Image
import csv
import re
import os
import login
import json
import userMenu

class resetPage : 
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')

        user_email = StringVar()
        user_password = StringVar()
        user_confirm_password = StringVar()

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
        self.heading = Label(self.lg_frame, text='RESET PASSWORD' , font=25 , bg='grey') 
        self.heading.place(x=8 , y=30 , width=634 , height=30)

        # =========back button===========
        self.back_button_photo = Image.open('images\\back.png')
        back_image=ImageTk.PhotoImage(self.back_button_photo)
        self.back_button = Button(self.lg_frame , image=back_image ,cursor="hand2" , background="grey" , relief=FLAT , command=self.loadLoginPage)
        self.back_button.image = back_image
        self.back_button.place(x=8 , y=30,width=50,height=50)

        # ========= email =========
        self.email_label = Label(self.lg_frame , text='email : ' , bg='grey' , font=(30))
        self.email_label.place(x=250 , y= 100 , width=150 , height=20)   

        self.email_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , highlightthickness=0 , textvariable=user_email)
        self.email_textbox.place(x=200 , y=130 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.email_line.place(x=200 , y=150)

        # ========= password =========
        self.password_label = Label(self.lg_frame , text='password : ' , bg='grey' , font=(30))
        self.password_label.place(x=250 , y= 200 , width=150 , height=20)   

        self.password_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , show='*' , textvariable=user_password)
        self.password_textbox.place(x=200 , y=230 , width=250 , height=20)

        self.password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.password_line.place(x=200 , y=250)

        # ========= confirm password =========
        self.confirm_password_label = Label(self.lg_frame , text=' confirm password : ' , bg='grey' , font=(30))
        self.confirm_password_label.place(x=250 , y= 300 , width=150 , height=20)   

        self.confirm_password_textbox = Entry(self.lg_frame , font=(25) , bg='grey' , relief='flat' , show='*' , textvariable=user_confirm_password)
        self.confirm_password_textbox.place(x=200 , y=330 , width=250 , height=20)

        self.confirm_password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='black' , highlightthickness=0 )
        self.confirm_password_line.place(x=200 , y=350)

        # ========= sign up button =========
        self.login_button = Image.open('images\\login_button.png')
        login_button_photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.lg_frame , image= login_button_photo , bg='grey')
        self.login_button_label.image = login_button_photo
        self.login_button_label.place(x=200 , y=420 , width=250 , height=50)

        self.login = Button(self.login_button_label , text='reset password' , font=(25) , bd=0 , cursor='hand2' , activeforeground='grey' , activebackground= '#1995CC', fg='black' , background='#1995CC' , command= lambda : self.validateAccount(self.email_textbox , self.password_textbox , self.confirm_password_textbox))
        self.login.place(x=55,y=10 ,width=130 )


    def loadPage(self):
        self.window.mainloop()

    def validateAccount(self,email_entry , password_entry , confirm_entry):
        user_email = email_entry.get()
        user_password = password_entry.get()
        confirm_password = confirm_entry.get()
        email_to_match = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

        if(user_password!=''):
            if(user_password!=confirm_password):
                print("please enter the correct password")
                return
        else:
            print('please enter a password')
            return
        
        
        if re.match(email_to_match,user_email):
            self.registerAccount(user_email , user_password)
            print('email is registered well')
        else:
            print('email invalid')
            return
        
    def registerAccount(self,user_email , user_password):
        # header = ['institution_name' , 'user_email' , 'user_password' ]
        old_data = []

        with open('users_account.csv' , 'r' , encoding='UTF8' , newline='') as r:
            reader = csv.reader(r)
            lines=0
            for row in reader:
                old_data.append(row)
        
            for data in old_data:
                if data[1] == user_email:
                    data[1] , data[2] = user_email , user_password
                    break
                print("email has not been registered yet")

        with open('users_account.csv' , 'w' , newline='') as w:
            writer = csv.writer(w)
            writer.writerows(old_data)

    def loadLoginPage(self):
        loginPage = login.loginForm(self.window)
        loginPage.loginPage()

# https://www.simplifiedpython.net/python-gui-login/, encoding='UTF8' , newline='\