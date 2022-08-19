from tkinter import *
import login

def init():
    window = Tk()
    firstPage = login.loginForm(window)
    firstPage.loginPage()

init()