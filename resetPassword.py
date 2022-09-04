from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox
import csv
import re
import login

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
        self.lg_frame = Frame(self.window , bg = 'black' , width=650 , height=550)
        self.lg_frame.place(x=258,y=100)

        # ========= heading =========
        self.heading = Label(self.lg_frame, text='RESET PASSWORD' , font=25 , bg='black' , fg='white') 
        self.heading.place(x=8 , y=30 , width=634 , height=30)

        # =========back button===========
        self.back_button_photo = Image.open('images\\back.png')
        back_image=ImageTk.PhotoImage(self.back_button_photo)
        self.back_button = Button(self.lg_frame , image=back_image ,cursor="hand2" , background="black" , relief=FLAT , command=self.loadLoginPage)
        self.back_button.image = back_image
        self.back_button.place(x=8 , y=10,width=50,height=50)

        # ========= email =========
        self.email_label = Label(self.lg_frame , text='email : ' , bg='black' , fg='white' , font=(30))
        self.email_label.place(x=250 , y= 100 , width=150 , height=20)   

        self.email_textbox = Entry(self.lg_frame , font=(25) , bg='black' , fg='white' , insertbackground='white' , relief='flat' , highlightthickness=0 , textvariable=user_email)
        self.email_textbox.place(x=200 , y=130 , width=250 , height=20)

        self.email_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.email_line.place(x=200 , y=150)

        # ========= password =========
        self.password_label = Label(self.lg_frame , text='password : ' , bg='black' , fg='white' , font=(30))
        self.password_label.place(x=250 , y= 200 , width=150 , height=20)   

        self.password_textbox = Entry(self.lg_frame , font=(25) , bg='black' ,fg='white' , insertbackground='white' , relief='flat' , show='*' , textvariable=user_password)
        self.password_textbox.place(x=200 , y=230 , width=250 , height=20)

        self.password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.password_line.place(x=200 , y=250)

        # ========= confirm password =========
        self.confirm_password_label = Label(self.lg_frame , text=' confirm password : ' , bg='black' , fg='white' , font=(30))
        self.confirm_password_label.place(x=250 , y= 300 , width=150 , height=20)   

        self.confirm_password_textbox = Entry(self.lg_frame , font=(25) , bg='black', fg='white' , insertbackground='white' , relief='flat' , show='*' , textvariable=user_confirm_password)
        self.confirm_password_textbox.place(x=200 , y=330 , width=250 , height=20)

        self.confirm_password_line = Canvas(self.lg_frame , width= 250 , height=2 , bg='white' , highlightthickness=0 )
        self.confirm_password_line.place(x=200 , y=350)

        # ========= reset button =========
        self.reset_button = Image.open('images\\login_button.png')
        reset_button_photo = ImageTk.PhotoImage(self.reset_button)
        self.reset_button_label = Label(self.lg_frame , image= reset_button_photo , bg='black')
        self.reset_button_label.image = reset_button_photo
        self.reset_button_label.place(x=200 , y=420 , width=250 , height=50)

        self.reset = Button(self.reset_button_label , text='reset' , font=(10) , bd=0 , cursor='hand2' , activeforeground='grey' , activebackground= '#1995CC', fg='black' , background='#1995CC' , command= lambda : self.validateAccount(self.email_textbox , self.password_textbox , self.confirm_password_textbox))
        self.reset.place(x=55,y=10 ,width=130 , height=30)


    def loadPage(self):
        self.window.mainloop()

    def validateAccount(self,email_entry , password_entry , confirm_entry):
        user_email = email_entry.get()
        user_password = password_entry.get()
        confirm_password = confirm_entry.get()
        email_to_match = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

        if(user_email == '' or user_password=='' or confirm_password==''):
            messagebox.showerror(title="Error" , message="Please fill in the required entries")
            return
        else:
            if(user_password!=confirm_password):
                messagebox.showerror(title="Error" , message="Please fill in the correct password")
                return
        
            if re.match(email_to_match,user_email):
                self.registerAccount(user_email , user_password)
            else:
                messagebox.showerror(title="Error" , message="Please fill in the correct email")
                return
        
    def registerAccount(self,user_email , user_password):
        # header = ['institution_name' , 'user_email' , 'user_password' ]
        old_data = []

        with open('users_account.csv' , 'r' , encoding='UTF8' , newline='') as r:
            reader = csv.reader(r)
            for row in reader:
                old_data.append(row)
            
            if user_email not in list(x[1] for x in old_data):
                messagebox.showerror(title="Error" , message="Email has not been registered yet")
                return

            for data in old_data:
                if data[1] == user_email:
                    data[1] , data[2] = user_email , user_password
                    break


        with open('users_account.csv' , 'w' , newline='') as w:
            writer = csv.writer(w)
            writer.writerows(old_data)
            messagebox.showinfo(message="Password has been reset")

    def loadLoginPage(self):
        loginPage = login.loginForm(self.window)
        loginPage.loginPage()

# https://www.simplifiedpython.net/python-gui-login/, encoding='UTF8' , newline='\