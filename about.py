from cgitb import text
from sys import dont_write_bytecode
from tkinter import *
from turtle import back, bgcolor, width, window_width
from PIL import ImageTk , Image
import os
import signup
from tkhtmlview import HTMLLabel
import userMenu

class aboutPage : 
        def __init__(self,window):
                self.window = window
                self.window.geometry('1166x718')
                menu = userMenu.createMenu(window)

                # =============about us=================  
                about = HTMLLabel(self.window, html="""
                <div style='background-color:#FFE4C4'>
                <h1 style="text-align:center">About us</h1>


                <p>This software allow users to download into their smart devices for video surveillance features. This is extremely 
                useful for individuals who wishes to capture any hindrance to their respective desired spots which may be of much value to you
                and you can develop a bigger sense of security after applying our software in your devices. Our software is extremely user-friendly and any
                individuals can download to enjoy this software features. </p>
                <p>Our aim is to develope an easy-to-use security camera software for every computer. All you need is just a camera for your computer and it will surveill for you.</p>
                <p>This software is developed by members of Team 60: Bevlyn Tan, Deepak, Dheran, Kenneth, Wei Shen </p>


                </div>
                """)

                about.config(bg='#FFE4C4')
                # Adjust label
                about.pack(pady=20, padx=20 , fill='both')

        def loadPage(self):
                self.window.mainloop()


