from distutils.cmd import Command
from json import load
from tkinter import *
from turtle import home
import manual
import about
import home
import setting
import json

class createMenu():
    def __init__(self , window):
        menu = Menu(window)
        self.window = window
        window.config(menu=menu , bg='#FFE4C4')
        with open('logging_in.json') as json_file:
            global user_dict 
            user_dict = json.load(json_file)

# =============home menu=================
        homeMenu = Menu(menu , tearoff=0 , activebackground='orange')

# =============help menu=================
        helpMenu = Menu(menu , tearoff=0 , activebackground='orange')
        helpMenu.add_command(label='home' , command=self.loadHome)
        helpMenu.add_command(label='about us' , command=self.loadAbout)
        helpMenu.add_command(label='user manual' , command=self.loadManual)
        menu.add_cascade(label='help' , menu=helpMenu)

# =============setting menu=================      
        settingMenu = Menu(menu , tearoff=0 , activebackground='orange')
        settingMenu.add_command(label='account setting' , command=self.loadSetting)
        settingMenu.add_command(label='log out')
        menu.add_cascade(label='setting' , menu=settingMenu)

# =============exit menu=================      
        exitMenu = Menu(menu , tearoff=0 , activebackground='orange')
        menu.add_cascade(label='exit' , menu=exitMenu)

    def loadHome(self):
        for widgets in self.window.winfo_children():
             widgets.destroy()
        homePage = home.homePage(self.window , user_dict["insti_name"])
        homePage.loadPage()

    def loadManual(self):
        for widgets in self.window.winfo_children():
             widgets.destroy()
        manualPage = manual.manualPage(self.window)
        manualPage.loadPage()

    def loadAbout(self):
        for widgets in self.window.winfo_children():
             widgets.destroy()
        aboutPage = about.aboutPage(self.window)
        aboutPage.loadPage()

    def loadSetting(self):
        for widgets in self.window.winfo_children():
         widgets.destroy()
        settingPage = setting.settingPage(self.window)
        settingPage.loadPage()
