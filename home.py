from cgitb import text
# from curses import window
from sys import dont_write_bytecode
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE
from turtle import back, home, width, window_width
from PIL import ImageTk , Image
import os
import signup
import userMenu

class homePage : 
    def __init__(self,window,institution = ""):
        self.window = window
        self.window.geometry('1166x718')
        menu = userMenu.createMenu(window)

# # =============logo =================           
#         self.logo = Image.open('images\\logo_1.jpg')
#         photo = ImageTk.PhotoImage(self.logo)
#         self.logo_panel = Label(self.window,image=photo)
#         self.logo_panel.image = photo
#         self.logo_panel.place(x=458 , y=50 , width=250 , height=250 )  

# # =============profile =================           
#         self.profile_wlc = Label(self.window , font=(100) , bg='#27285C' , fg='white' , text="Welcome back!" , justify='center')
#         self.profile_wlc.place(x=358 , y=320 , width=450)

#         self.profile = Label(self.window , font=(100) , bg='#27285C' , fg='white' , text="This security camera is currently working for "+ institution , justify='center')
#         self.profile.place(x=258 , y=350 , width=650)

# # =============recording button =================        
#         self.record_button = Button(self.window , text='Start recording' , font=(50)  , cursor='hand2' , command=startRecording)
#         self.record_button.place(x=458,y=400 , width=250 , height=150 )
#         self.record_button.bind('<Enter>' , on_enter)
#         self.record_button.bind('<Leave>' , on_leave)
        # Create A Canvas
        my_canvas = Canvas(self.window)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(self.window, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        #Load an image in the script

        self.img= (Image.open("images\\icon1.png"))
        self.img1=(Image.open("images\\surv.png"))
        self.img2=(Image.open("images\\recorder.png"))
        self.img3=(Image.open("images\\detector.png"))
        self.img4=(Image.open("images\\email.png"))
        #Resize the Image using resize method
        # icon image
        resized_image= self.img.resize((200,150), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resized_image)
        # surv image
        resized_image1= self.img1.resize((100,150), Image.ANTIALIAS)
        self.new_image1= ImageTk.PhotoImage(resized_image1)
        # recorder image
        self.resized_image2= self.img2.resize((100,150), Image.ANTIALIAS)
        self.new_image2= ImageTk.PhotoImage(self.resized_image2)
        # dectector image
        self.resized_image3= self.img3.resize((100,150), Image.ANTIALIAS)
        self.new_image3= ImageTk.PhotoImage(self.resized_image3)
        # email image
        self.resized_image4= self.img4.resize((100,150), Image.ANTIALIAS)
        self.new_image4= ImageTk.PhotoImage(self.resized_image4)


        #Add image to the Canvas Items
        my_canvas.create_image(0,0, anchor=NW, image=self.new_image)
        my_canvas.create_image(55,500, anchor=NW, image=self.new_image1)
        my_canvas.create_image(600,500, anchor=NW, image=self.new_image2)
        my_canvas.create_image(55,700, anchor=NW, image=self.new_image3)
        my_canvas.create_image(600,700, anchor=NW, image=self.new_image4)

        my_canvas.create_text((600,77), text="Welcome Back!",font=('Arial',40,'bold'),anchor=CENTER)
        my_canvas.create_text((600,195), text="This security camera is currently waiting for test",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((385,550), text="Video Surveillance:\nis installed on your smart devices, \nEasy Cam uses IP cameras and \nwebcams to perform unbeatable video monitoring. \nThe program supports more than 1200 models \nof IP cameras, and virtually all webcams.",
        font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((850,550), text="Video Recording: \nuses Opencv encoding engine for \nquality video recording. You can \nrecord the events in your home, \noffice or shop while you are away. \nYou can run recording at special \nperiods of a day and the week.",
        font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((385,800), text="Motion detector: \nis one of the main tools available \nin Easy Cam. It is based on the \nvideo frame analyzing algorihm. You \ncan use it to protect your home \nor company from intruders. The motion \nsensor and masking tool are fully \ncustomizable so you can be sure you will \nnot get the false alerts.",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((900,800), text="Alerts via Email & SMS: \nIf Easy Cam detects motion, it \nwill start recording. It \ncan also send you an alert message to \nyour email, with attached video from \ncameras. Therefore, you will be able \nto safely keep a footage of the incident \nin your own mail-box. In addition, \nyou also can anytime view the video on \nyour mail-box anywhere and anytime, even \nmore so better for tracking evidence",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((600,1000), text="Typical Scenarios and Uses",font=('Arial',35,'bold'),anchor=CENTER)
        my_canvas.create_text((385,1140), text="1. Home Security \nKeep an eye on your home when you \nare away. Just install Security Eye software, \nand use existing USB webcam connected to your \ncomputer. Your home security system is complete! \nNow in case of intrusion, you'll instantly \nbe alerted with photos of the thieves sent \nto your email and mobile.",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((850,1115), text="2. Baby Surveillance \nKeep a constant eye on your child anytime, \nanywhere. Follow what is happening in your baby's \nroom when you are away. Do you have any \nsuspicions about your nanny? Use Security Eye to \ncollect an evidence - you'll have it all on tape!",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((360,1300), text="3. Pet Monitoring \nHave you ever wondered what your favorite \nanimal is doing while you are not at home? \nWith the help of EasyCam now and \ncreate the next buzz on YouTube.",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((850,1290), text="4. Business Monitoring\nAs well as your home, your office \nor retail store also needs a good security \nsystem. At night, you can use it as a \nmotion detection system, and on working hours - \nfor recording the work process. Your staff \nneeds to be monitored as well! WIth Easycam, \nyou'll always know what's happening at work.",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((360,1440), text="5. Theft Prevention \nAdvanced object recognition and AI \ncut down on false alerts whilst protecting \nyour investments. Recordings can be saved \nlocally and to the cloud - ensuring evidence \nis secure even if the device itself is stolen.",font=('Arial',13,'bold'),anchor=CENTER)
        my_canvas.create_text((820,1440), text="6. Wildlife Watching \nA discrete webcam reveals a wonderful \nworld of wildlife. Agent DVR can record \nmovement in a burrow or nest and send it \nstraight to your email or mobile device.",font=('Arial',13,'bold'),anchor=CENTER)
        
        self.group_photo_image = Image.open("images\\group_photo.jpg")
        self.resized_image5=self.group_photo_image.resize((450,270) , Image.ANTIALIAS)
        self.group_photo = ImageTk.PhotoImage(self.resized_image5)
        my_canvas.create_image(100,1590 , anchor=NW , image=self.group_photo)
        my_canvas.create_text((780,1590), text="About Us",font=('Arial',40,'bold'),anchor=CENTER)
        my_canvas.create_text((860,1750), text="Easy Cam is created by Team 60, whose members\nare Dharen, Deepak, Kenneth, WeiShen and Bevlyn.\nFive of us has created Easy Cam for users\nwho wish to enhance their own security needs. \nEasy Cam is here to help them develop a better sense of\nsecurity so that users of our software can enjoy their daily \nleisure activities without stressing about the consequences.",font=('Arial',14,'bold'),anchor=CENTER)

        # button to start program
        self.btn_inactive_image = Image.open("images\\Button_inactive.png")
        self.btn_active_image = Image.open("images\\Button_active.png")

        self.btn_inactive=ImageTk.PhotoImage(self.btn_inactive_image)
        self.btn_active=ImageTk.PhotoImage(self.btn_active_image)

        button=Button(self.window, image=self.btn_inactive, width=300, height=150, bd=0, relief="sunken", command=pressed)
        my_canvas.create_window(582,340, window=button)
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)

    def loadPage(self):
        self.window.mainloop()

    def on_enter(self,event):
        event.widget["image"]=self.btn_active
    def on_leave(self,event):
        event.widget["image"]=self.btn_inactive

def startRecording():
        os.system('python site-packages\cam.py')


def pressed():
        print("button is pressed")

#    https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change