import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter import font

def remove_all_widgets(parent):
    for widget in parent.winfo_children():
        widget.destroy()

def logIn():
    remove_all_widgets(root)
    return

def register():
    return

def storeLocator():
    return

def home():
    return

def profile():
    return

def basket():
    return

def checkout():
    return

def orderedScreen():
    return

# Create the main window
root = Tk()
root.geometry("300x500")
root.resizable(False, False)
# Background
background = "#D2B48C" # Color
root.config(bg=background) # Change root
s = Style() # ttk frame
s.configure("TFrame", background="blue") # Set color of ttk frame
custom_font = font.Font(family="Arial", size=22, weight="bold")

logo = Label(root, text="Beans and Brew Cafe", font=custom_font, background="red")
logo.place(x=0, y=0, height=50)

mainFrame = Frame(root, style="TFrame")
mainFrame.place(width=300, height=400, x=0, y=50)

openButton = Button(mainFrame, text="Login", command=logIn)
openButton.place(width=100, height=100, x=100, y=150)


# Run the Tkinter event loop
root.mainloop()
