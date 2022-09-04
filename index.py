from tkinter import *
import login

def init():
    window = Tk()
    icon=PhotoImage(file='images\\icon.png')
    window.iconphoto(TRUE,icon)
    window.title("EASY CAM")
    firstPage = login.loginForm(window)
    firstPage.loginPage()

init()