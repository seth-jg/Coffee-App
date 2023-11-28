import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter import font

# removes all the widgets from the screen/ frame
def remove_all_widgets(parent):
    for widget in parent.winfo_children():
        widget.destroy()

def logInScreen():
    remove_all_widgets(mainFrame)

    # Labels
    logLabel = Label(mainFrame, text="Log In", font=header_font)
    userLabel = Label(mainFrame, text="Enter username: ")
    passwordLabel = Label(mainFrame, text="Enter password: ")

    # Entry bars
    user = Entry(mainFrame)
    password = Entry(mainFrame)

    # Buttons
    loginButton = Button(mainFrame, text="Login", command=logIn)
    signupButton = Button(mainFrame, text="Sign up", command=register)

    # Layout
    logLabel.place(width=80, x=110, y=20)

    userLabel.place(width=150, x=50, y=75)
    user.place(width=200, x=50, y=100)
    passwordLabel.place(width=150, x=50, y=150)
    password.place(width=200, x=50, y=175)

    loginButton.place(width=80, x=60, y=240)
    signupButton.place(width=80, x=160, y=240)

def register():
    remove_all_widgets(mainFrame)
    return

def storeLocator():
    remove_all_widgets(mainFrame)
    return

def home():
    remove_all_widgets(mainFrame)
    return

def profile():
    remove_all_widgets(mainFrame)
    return

def basket():
    remove_all_widgets(mainFrame)
    return

def checkout():
    remove_all_widgets(mainFrame)
    return

def orderedScreen():
    remove_all_widgets(mainFrame)
    return

#this is used to see if the user is registering or logging in
registerCheck = 0

# Create the main window
root = Tk()
root.geometry("300x500")
root.resizable(False, False)
# Background
background = "#D2B48C" # Color
root.config(bg=background) # Change root

# Font
custom_font = font.Font(family="Arial", size=22, weight="bold")
header_font = font.Font(family="Arial", size=18)

# setting the styles
mainStyle = Style()
nBarStyle = Style()

# Configure styles for main frame and navigation bar frame
mainStyle.configure("Main.TFrame", background="blue")
nBarStyle.configure("NavBar.TFrame", background="red")


# Main
# Title bar
logo = Label(root, text="Beans and Brew Cafe", font=custom_font, background="red")
logo.place(x=0, y=0, height=50)

# Where teh myjority of content will fit in
mainFrame = Frame(root, style="Main.TFrame")
mainFrame.place(width=300, height=400, x=0, y=50)

# Start the app
openButton = Button(mainFrame, text="Login", command=logInScreen)
openButton.place(width=100, height=100, x=100, y=150)

# Nav bar
navFrame = Frame(root, style="NavBar.TFrame")
navFrame.place(width=300, height=50, x=0, y=450)

# Nav buttons
homeButton = Button(navFrame, text="Home")
basketButton = Button(navFrame, text="Basket")
profileButton = Button(navFrame, text="Profile")

homeButton.place(width=80, height=30, x=20, y=10)
basketButton.place(width=80, height=30, x=110, y=10)
profileButton.place(width=80, height=30, x=200, y=10)

# Run the Tkinter event loop
root.mainloop()
