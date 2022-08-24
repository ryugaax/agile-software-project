from cgitb import text
from decimal import Overflow
from sys import dont_write_bytecode
from tkinter import *
from turtle import back, bgcolor, right, width, window_width
from PIL import ImageTk , Image
import os
import signup
from tkhtmlview import HTMLLabel
import userMenu

class manualPage : 
        def __init__(self,window):
                self.window = window
                self.window.geometry('1166x718')
                menu = userMenu.createMenu(window)
                # =============about us=================  
                about = HTMLLabel(self.window, html="""
                <div style='background-color:#FFE4C4' style='padding-left:auto ; padding-right:auto'>
                <h1 style="text-align:center"><u>How To Use</u></h1>

                <img src='images/manual_1.jpg' width='500' height='300' style='padding-left:auto ; padding-right:auto'>
                <br>
                <br>
                <br>
                <br>
                <img src='images/manual_2.png' width='500' height='300' style='padding-left:auto ; padding-right:auto'>
                <br>
                <br>
                <br>
                <br>
                <img src='images/manual_3.png' width='500' height='300' style='padding-left:auto ; padding-right:auto'>
                <br>
                <br>
                </div>
                """)

                about.config(bg='black' , height=718 , )
                # Adjust label
                about.pack(pady=20, padx=20 , fill='both')

        def loadPage(self):
                self.window.mainloop()
