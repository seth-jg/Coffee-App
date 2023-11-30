import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from random import randint
from DatabaseFunctions import *
from AccountHandling import *

# Create root screen
root = Tk()
root.geometry("300x500")
root.resizable(False, False)

# store users info
_user = Account()
_shop = ""
_total = 0

# 2d array for customers basket
_basketArray = [] 

# Colors
background =  "#c69f6c"
itemColor = "#D2B48C"
root.config(bg=background) # Change root background

# Font
custom_font = font.Font(family="Arial", size=22, weight="bold")
header_font = font.Font(family="Arial", size=18)

# setting the styles
mainStyle = Style()
nBarStyle = Style()
itemStyle = Style()

# Configure styles for main frame and navigation bar frame
mainStyle.configure("Main.TFrame", background=background)
nBarStyle.configure("NavBar.TFrame", background="red")
itemStyle.configure("item.TFrame", background=itemColor)


def starter_screen():
    global mainFrame
    global homeButton
    global basketButton
    global profileButton

    # Title bar
    logo = Label(root, text="Beans and Brew Cafe", font=custom_font, background="red")
    logo.place(x=0, y=0, height=50)

    # Where teh myjority of content will fit in
    mainFrame = Frame(root, style="Main.TFrame")
    mainFrame.place(width=300, height=400, x=0, y=50)

    # Start the app
    #openButton = Button(mainFrame, text="Login", command=login_screen)
    openButton = Button(mainFrame, text="Login", command=store_locator)
    openButton.place(width=100, height=100, x=100, y=150)

    # Nav bar
    navFrame = Frame(root, style="NavBar.TFrame")
    navFrame.place(width=300, height=50, x=0, y=450)

    # Nav buttons
    homeButton = Button(navFrame, text="Home", state="disabled", command=home)
    basketButton = Button(navFrame, text="Basket", state="disabled", command=basket)
    profileButton = Button(navFrame, text="Profile", state="disabled", command=profile)

    homeButton.place(width=80, height=30, x=20, y=10)
    basketButton.place(width=80, height=30, x=110, y=10)
    profileButton.place(width=80, height=30, x=200, y=10)

    # Remove these when done
    homeButton.config(state="enabled")
    basketButton.config(state="enabled")
    profileButton.config(state="enabled")
    ord = Button(mainFrame, text="order", command=ordered_screen)
    ord.place(width=100, x=100, y=300)
    chec = Button(mainFrame, text="checkout", command=checkout_screen)
    chec.place(width=100, x=100, y=350)

    # Run the Tkinter event loop
    root.mainloop()


# removes all the widgets from the screen/ frame
def remove_all_widgets(parent):
    for widget in parent.winfo_children():
        widget.destroy()


# put at the end of any function that is a gui if want
def add_color_to_all_widgets(parent):
    for widget in parent.winfo_children():
        if isinstance(widget, Label):
            widget.config(background=itemColor)


# Verify functions
def login_verify(user, pword):
    userInfo = get_user_info(user, pword)
    if userInfo:
        _user = Account(userInfo)
        homeButton.config(state="normal")
        basketButton.config(state="normal")
        profileButton.config(state="normal")
        store_locator()
    else:
        userIncorect.config(text="Username or Password Incorect")


def register_verify(user, pword, pcode, mobi):
    if not check_username_exists(user):
        create_new_user(user, pword, pcode, mobi)
        _user = Account(user, pword, pcode, mobi)
        homeButton.config(state="normal")
        basketButton.config(state="normal")
        profileButton.config(state="normal")
        store_locator()
    else:
        accountExists.config(text="Account already exists")

# Login screen
def login_screen():
    global userIncorect
    remove_all_widgets(mainFrame)

    # Labels
    logLabel = Label(mainFrame, text="Log In", font=header_font)
    userLabel = Label(mainFrame, text="Enter username: ")
    passwordLabel = Label(mainFrame, text="Enter password: ")
    userIncorect = Label(mainFrame, text="")

    # Entry bars
    user = Entry(mainFrame)
    password = Entry(mainFrame, show="*")

    # Buttons
    loginButton = Button(mainFrame, text="Login", command = lambda: login_verify(user.get(), password.get()))
    signupButton = Button(mainFrame, text="Sign up", command=register)

    # Layout
    logLabel.place(width=80, x=110, y=10)

    userLabel.place(width=150, x=50, y=75)
    user.place(width=200, x=50, y=100)
    passwordLabel.place(width=150, x=50, y=150)
    password.place(width=200, x=50, y=175)

    loginButton.place(width=80, x=60, y=240)
    signupButton.place(width=80, x=160, y=240)

    userIncorect.place(width=180, x=60, y=280)


# Sign up screen
def register():
    global accountExists
    remove_all_widgets(mainFrame)

    # Labels
    regLabel = Label(mainFrame, text="Sign up", font=header_font)
    userLabel = Label(mainFrame, text="Enter username: ")
    passwordLabel = Label(mainFrame, text="Enter password: ")
    postcodeLabel = Label(mainFrame, text="Enter postcode: ")
    mobileLabel = Label(mainFrame, text="Enter mobile: ")
    accountExists = Label(mainFrame)

    # Entry bars
    user = Entry(mainFrame)
    password = Entry(mainFrame, show="*")
    postcode = Entry(mainFrame)
    mobile = Entry(mainFrame)

    # Buttons
    signupButton = Button(mainFrame, text="Sign up", command= lambda: register_verify(user.get(), password.get(), postcode.get(), mobile.get()))
    loginButton = Button(mainFrame, text="Login", command=login_screen)

    # Layout
    regLabel.place(width=100, x=110, y=10)

    userLabel.place(width=150, x=50, y=75)
    user.place(width=200, x=50, y=100)

    passwordLabel.place(width=150, x=50, y=140)
    password.place(width=200, x=50, y=165)

    postcodeLabel.place(width=150, x=50, y=205)
    postcode.place(width=200, x=50, y=230)

    mobileLabel.place(width=150, x=50, y=270)
    mobile.place(width=200, x=50, y=295)

    loginButton.place(width=80, x=160, y=340)
    signupButton.place(width=80, x=60, y=340)

    accountExists.place(width=124, x=88, y=370)


def store_located():
    return

# Store locator screen
def store_locator():
    remove_all_widgets(mainFrame)
    locations = get_all_store_locations()
    positiony = 0
    
    # Title of the page
    regLabel = Label(mainFrame, text="Store Locator", font=header_font)
    regLabel.place(width=155, x=75, y=10)

    # Menu frame
    storeFrame = Frame(mainFrame)
    storeFrame.place(width=300, height=350, x=0, y=50)

    # Add for loop to create the content for products
    for n, location in enumerate(locations):
        item = Label(storeFrame, text=location)
        item.place(x=0)
        itemFrame = Frame(storeFrame)
        itemFrame.config(style="item.TFrame" if n % 2 == 0 else "Main.TFrame")
        itemFrame.place(width=300, height=50, x=0, y=positiony)
        positiony += 50
    

# Home screen
def home():
    remove_all_widgets(mainFrame)
    productArray = get_all_products()
    positiony = 0
    print(productArray)

    # Title of the page
    regLabel = Label(mainFrame, text="Menu", font=header_font)
    regLabel.place(width=100, x=110, y=10)

    # Menu frame
    menuFrame= Frame(mainFrame)
    menuFrame.place(width=300, height=350, x=0, y=50) 

# Profile screen
def profile():
    remove_all_widgets(mainFrame)

    # Labels
    regLabel = Label(mainFrame, text="Sign up", font=header_font)
    userLabel = Label(mainFrame, text="Enter username: ")
    passwordLabel = Label(mainFrame, text="Enter password: ")
    postcodeLabel = Label(mainFrame, text="Enter postcode: ")
    mobileLabel = Label(mainFrame, text="Enter mobile: ")

    user = Label(mainFrame, text=_user.user)
    password = Label(mainFrame, text="*"*len(_user.password))
    postcode = Label(mainFrame, text=_user.postcode)
    mobile = Label(mainFrame, text=_user.mobile)

    # Buttons
    signOutButton = Button(mainFrame, text="SignOut", command=starter_screen)

    # Layout
    regLabel.place(width=100, x=110, y=10)

    userLabel.place(width=150, x=50, y=75)
    user.place(width=200, x=50, y=100)

    passwordLabel.place(width=150, x=50, y=140)
    password.place(width=200, x=50, y=165)

    postcodeLabel.place(width=150, x=50, y=205)
    postcode.place(width=200, x=50, y=230)

    mobileLabel.place(width=150, x=50, y=270)
    mobile.place(width=200, x=50, y=295)

    signOutButton.place(width=60, x=120, y=340)
    

# Basket screen
def basket():
    remove_all_widgets(mainFrame)

    # Title of the page
    regLabel = Label(mainFrame, text="Basket", font=header_font)
    regLabel.place(width=100, x=110, y=10)

    # Basket frame
    basketFrame= Frame(mainFrame)
    basketFrame.place(width=300, height=300, x=0, y=50)

    # Add forloop to create the content for products
    
    # Checkout button
    checkoutButton = Button(mainFrame, text="checkout", command=checkout_screen)
    checkoutButton.place(width=80, height=30, x=110, y=360)

    if len(_basketArray) == 0:
        checkoutButton.config(state="disabled") 


# Checkout screen
def checkout_screen():
    remove_all_widgets(mainFrame)
    
    # Title of the page
    regLabel = Label(mainFrame, text="Checkout", font=header_font)
    regLabel.place(width=120, x=90, y=10)

    # Store label
    storeLabel = Label(mainFrame, text=f"Store: {_shop}")
    storeLabel.place(width=150, x=0, y=50)

    # Item total
    storeLabel = Label(mainFrame, text=f"Total: £{_total}")
    storeLabel.place(width=120, x=180, y=50)

    # Item veiwer
    itemFrame= Frame(mainFrame)
    itemFrame.place(width=300, height=120, x=0, y=70)

    # Add forloop to create the content for products

    # Card information
    # Labels 
    nameOnCardLabel = Label(mainFrame, text="Name on card")
    cardNumberLabel = Label(mainFrame, text="Card number")
    cvv2Label = Label(mainFrame, text="CVV2")

    # Entry
    nameOnCard = Entry(mainFrame)
    cardNumber = Entry(mainFrame)
    cvv2 = Entry(mainFrame)
    
    # Layout
    nameOnCardLabel.place(width=150, x=50, y=200)
    nameOnCard.place(width=200, x=50, y=220)
    cardNumberLabel.place(width=150, x=50, y=250)
    cardNumber.place(width=200, x=50, y=270)
    cvv2Label.place(width=150, x=50, y=300)
    cvv2.place(width=200, x=50, y=320)

    # Pay button
    payButton = Button(mainFrame, text="Pay")
    payButton.place(width=80, height=30, x=110, y=360)

# Order screen
def ordered_screen():
    remove_all_widgets(mainFrame)

    # Title of the page
    regLabel = Label(mainFrame, text=f"Order # {randint(100000, 999999)}", font=header_font)
    regLabel.place(width=300, x=0, y=10)


if __name__ == "__main__":
    starter_screen()