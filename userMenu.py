from distutils.cmd import Command
from tkinter import *
from turtle import home
import login
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
        menu.add_cascade(label='help' , menu=helpMenu)

# =============setting menu=================      
        settingMenu = Menu(menu , tearoff=0 , activebackground='orange')
        settingMenu.add_command(label='account setting' , command=self.loadSetting)
        settingMenu.add_command(label='log out' , command=self.logOut)
        settingMenu.add_separator()
        settingMenu.add_command(label='exit' , command=self.quitWindow)
        menu.add_cascade(label='setting' , menu=settingMenu)


    def loadHome(self):
        for widgets in self.window.winfo_children():
             widgets.destroy()
        homePage = home.homePage(self.window , user_dict["insti_name"])
        homePage.loadPage()

    def loadSetting(self):
        for widgets in self.window.winfo_children():
            widgets.destroy()
        settingPage = setting.settingPage(self.window)
        settingPage.loadPage()
    
    def quitWindow(self):
        self.window.destroy()

    def logOut(self):
        for widgets in self.window.winfo_children():
            widgets.destroy()
        with open("logging_in.json", "w") as outfile:
            user_dict={}
            json.dump(user_dict, outfile)
        loginPage = login.loginForm(self.window)
        loginPage.loginPage() 
