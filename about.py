from cgitb import text
from sys import dont_write_bytecode
from tkinter import *
from turtle import back, bgcolor, width, window_width
from PIL import ImageTk , Image
import os
import signup
from tkhtmlview import HTMLLabel

class homePage : 
    def __init__(self,window):
        self.window = window
        self.window.geometry('1166x718')
        menu = Menu(window)
        window.config(menu=menu , bg='#2832C2')

# =============help menu=================
        helpMenu = Menu(menu , tearoff=0 , activebackground='orange')
        helpMenu.add_command(label='how to use')
        helpMenu.add_command(label='about us')
        menu.add_cascade(label='help' , menu=helpMenu)

# =============setting menu=================      
        settingMenu = Menu(menu , tearoff=0 , activebackground='orange')
        settingMenu.add_command(label='account setting')
        settingMenu.add_command(label='log out')
        menu.add_cascade(label='setting' , menu=settingMenu)

# =============exit menu=================      
        exitMenu = Menu(menu , tearoff=0 , activebackground='orange')
        menu.add_cascade(label='exit' , menu=exitMenu)

# =============about us=================  
        about = HTMLLabel(self.window, html="""
            <div style='background-color:#2832C2'>
            <h1 style="text-align:center">About us</h1>
            
        
            <p>Agile Security Cam is developed by Team60 from the Agile Software Project module in UOL Computer Science programme.</p>
            <p>Our aim is to develope an easy-to-use security camera software for every computer. All you need is just a camera for your computer and it will surveill for you.</p>
            <ul>This software is developed by : 
            <li>bev</li>
            <li>deepak</li>
            <li>dharen</li>
            <li>kenneth</li>
            <li>wei shen</li>
            </ul>
            </div>
            """)
        
        about.config(bg='#2832C2')
        # Adjust label
        about.pack(pady=20, padx=20 , fill='both')

def page():
    window = Tk()
    homePage(window)
    window.mainloop()

page()
