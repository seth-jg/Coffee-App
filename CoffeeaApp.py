import sqlite3
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from random import randint
from DatabaseFunctions import *
from AccountHandling import *
from PIL import Image, ImageTk

'''
INDEX (lines) may change from code edits
---------
Root screen: 31
Main Variables: 37
Starter screen: 78
Widget change and remove: 123
Popup screen: 136
Reset variables: 150
Login screen: 166
Register: 219
Store locator: 186
Menu/ home screen: 376
Veiw orders: 481
Profile:
Basket:
Checkout:
Payment:
Ordered screen:


BUGS
--------
- shop not locating properly. Always printing tje last stor in the list
- Curly brackets arount all items past the 1st page in basket but not home page


TODO
-------
Account settings. Should be somewhat easy as i have already created the claass that can manipulate the account
Order page
'''


# Create root screen
root = Tk()
root.geometry("300x500")
root.resizable(False, False)

# store users info
_user = ""
_password = ""
_postcode = ""
_mobile = ""
_shopID = ""
_shop = ""
_total = 0
_orderNumber = 0
logo_path = "beansandbrewLOGO_resized.jpg"
background_path = "coffeeBack.jpg"

# 2d array for customers basket
_basketDictionary = {} 

# Colors
background =  "#c69f6c"
itemColor = "#B09775"
root.config(bg=background) # Change root background

# Font
custom_font = font.Font(family="Arial", size=22, weight="bold")
header_font = font.Font(family="Arial", size=18)
small_header = font.Font(family="Arial", size=14)

# setting the styles
mainStyle = Style()
nBarStyle = Style()
itemStyle = Style()

# Configure styles for main frame and navigation bar frame
mainStyle.configure("Main.TFrame", background=background)
nBarStyle.configure("NavBar.TFrame", background=itemColor)
itemStyle.configure("item.TFrame", background=itemColor)


def starter_screen():
    global mainFrame
    global homeButton
    global basketButton
    global profileButton

    # Title bar
    logo = Label(root, text="Beans and Brew Cafe", font=custom_font, background=itemColor)
    logo.place(x=0, y=0, height=50)

    # Where the myjority of content will fit in
    mainFrame = Frame(root, style="Main.TFrame")
    mainFrame.place(width=300, height=400, x=0, y=50)


    logo_img = ImageTk.PhotoImage(Image.open(logo_path))
    logo_label = Label(mainFrame, image=logo_img, background=background)
    logo_label.place(x=50, y=10, width=200, height=200)


    # Start the app
    loginButton = Button(mainFrame, text="Login", command=login_screen)
    loginButton.place(width=100, height=50, x=100, y=240)

    signupButton = Button(mainFrame, text="Sign up", command=register)
    signupButton.place(width=100, height=50, x=100, y=310)


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


def show_popup(title="Popup Window", message="This is a popup", time=1400):
    popup = Toplevel(root)
    popup.title(title)
    
    popup.config(background=background)
    popup.geometry("200x75")

    label = Label(popup, text=message, background=background)
    label.pack(padx=10, pady=20)

    # Schedule the destruction of the popup after 2000 milliseconds (2 seconds)
    popup.after(time, popup.destroy)


def reset_variables():
    global _basketDictionary, _shopID, _shop, _total, _orderNumber, basketCurrentPage, storeCurrentPage, menuCurrentPage, checkCurrentPage, orderCurrentPage
    _basketDictionary = {}
    _shopID = ""
    _shop = ""
    _total = 0
    _orderNumber = 0
    basketCurrentPage = 1
    storeCurrentPage = 1
    menuCurrentPage = 1
    checkCurrentPage = 1
    orderCurrentPage = 1


# Verify functions
def login_verify(user, pword):
    userInfo = get_user_info(user, pword)
    if userInfo:
        global _user
        global _password
        global _postcode
        global _mobile
        _user = userInfo[0]
        _password = userInfo[1]
        _postcode = userInfo[2]
        _mobile = userInfo[3]
        homeButton.config(state="normal")
        basketButton.config(state="normal")
        profileButton.config(state="normal")
        store_locator()
        show_popup("Logged In", f"Logged in as {user}")
    else:
        userIncorect.config(text="Username or Password Incorect")

# Login screen
def login_screen():
    global userIncorect
    remove_all_widgets(mainFrame)

    # Labels
    logLabel = Label(mainFrame, text="Log In", font=header_font, background=background)
    userLabel = Label(mainFrame, text="Enter username: ", background=background)
    passwordLabel = Label(mainFrame, text="Enter password: ", background=background)
    userIncorect = Label(mainFrame, text="", background=background)

    # Entry bars
    user = Entry(mainFrame)
    password = Entry(mainFrame, show="*")

    # Buttons
    loginButton = Button(mainFrame, text="Login", command = lambda: login_verify(user.get(), password.get()))
    starterButton = Button(mainFrame, text="Back", command=starter_screen)

    # Layout
    logLabel.place(width=80, x=110, y=10)

    userLabel.place(width=150, x=50, y=75)
    user.place(width=200, x=50, y=100)
    passwordLabel.place(width=150, x=50, y=150)
    password.place(width=200, x=50, y=175)

    loginButton.place(width=80, x=60, y=240)
    starterButton.place(width=80, x=160, y=240)

    userIncorect.place(width=180, x=60, y=280)


def register_verify(user, pword, pcode, mobi):
    if not check_username_exists(user):
        create_new_user(user, pword, pcode, mobi)
        global _user
        global _password
        global _postcode
        global _mobile
        _user = user
        _password = pword
        _postcode = pcode
        _mobile = mobi
        homeButton.config(state="normal")
        basketButton.config(state="normal")
        profileButton.config(state="normal")
        store_locator()
        show_popup("Registered", f"Registered user: {user}")
    else:
        accountExists.config(text="Account already exists")


# Sign up screen
def register():
    global accountExists
    remove_all_widgets(mainFrame)

    # Labels
    regLabel = Label(mainFrame, text="Sign up", font=header_font, background=background)
    userLabel = Label(mainFrame, text="Enter username: ", background=background)
    passwordLabel = Label(mainFrame, text="Enter password: ", background=background)
    postcodeLabel = Label(mainFrame, text="Enter postcode: ", background=background)
    mobileLabel = Label(mainFrame, text="Enter mobile: ", background=background)
    accountExists = Label(mainFrame, background=background)

    # Entry bars
    user = Entry(mainFrame)
    password = Entry(mainFrame, show="*")
    postcode = Entry(mainFrame)
    mobile = Entry(mainFrame)

    # Buttons
    signupButton = Button(mainFrame, text="Sign up", command= lambda: register_verify(user.get(), password.get(), postcode.get(), mobile.get()))
    starterButton = Button(mainFrame, text="Back", command=starter_screen)

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

    starterButton.place(width=80, x=160, y=340)
    signupButton.place(width=80, x=60, y=340)

    accountExists.place(width=124, x=88, y=370)


storeCurrentPage = 1
def store_next_page(storeLastPage):
    global storeCurrentPage
    if storeCurrentPage != storeLastPage:
        storeCurrentPage += 1
        home()

def store_previous_page():
    global storeCurrentPage
    if storeCurrentPage != 1:
        storeCurrentPage -= 1
        home()

def store_located(id, shop):                                   
    global _shop
    global _shopID
    _shop = shop
    _shopID = id
    show_popup("Store Located", f"You selected: {shop}")
    home()

# Store locator screen
def store_locator():
    remove_all_widgets(mainFrame)
    locations = get_all_store_locations() # gets a list of all the store locations
    positiony = 0 # y position for content
    pageCounter = 1 # used for labeling each page for the pages dictionary. Then used as a last page monitor
    counter = 0
    pageContent = []
    pages = {}

    for id, location in locations:
        counter += 1
        if counter %6 == 0:
            pages[pageCounter] = pageContent
            pageContent.clear()
            pageCounter += 1
        else:
            pageContent.append([id, location])
    pages[pageCounter] = pageContent
    # print(pages)
    
    # Title of the page
    regLabel = Label(mainFrame, text="Store Locator", font=header_font, background=background)
    regLabel.place(width=155, x=75, y=10)

    # store frame
    storeFrame = Frame(mainFrame, style="Main.TFrame")
    storeFrame.place(width=300, height=350, x=0, y=50)

    counter = 0
    # Add for loop to create the content for products
    for id, location in pages[storeCurrentPage]:
        # print(location)
        
        locationFrame = Frame(storeFrame)
        locationFrame.place(width=300, height=50, x=0, y=positiony)
        locationFrame.config(style="Main.TFrame")
        item = Label(locationFrame, text=location, background=background)
        item.place(width=150, height=20, x=20, y=15)

        counter += 1
        positiony += 50

        selectButton = Button(locationFrame, text="Select", command=lambda: store_located(id, location))
        selectButton.place(width=70, height=30, y=10, x=210)
    
    global storeBackButton
    global storeNextButton
    pageControlFrame = Frame(mainFrame, style="Main.TFrame")
    storeBackButton = Button(pageControlFrame, text="<--", command=store_previous_page)
    pageLabel = Label(pageControlFrame, text=f"Page {storeCurrentPage}", background=background)
    storeNextButton = Button(pageControlFrame, text="-->", command=lambda: menu_next_page(pageCounter))

    pageControlFrame.place(width=300, height=50, x=0, y=350)
    storeBackButton.place(width=70, height=30, y=10, x=18)
    pageLabel.place(width=40, height=30, y=10, x=130)
    storeNextButton.place(width=70, height=30, y=10, x=212)

    if storeCurrentPage == 1:
        storeBackButton.configure(state="disabled")
    else:
        storeBackButton.configure(state="normal")

    if storeCurrentPage == pageCounter:
        storeNextButton.configure(state="disabled")
    else:
        storeNextButton.configure(state="normal")
    

menuCurrentPage = 1
def menu_next_page(menuLastPage):
    global menuCurrentPage
    if menuCurrentPage != menuLastPage:
        menuCurrentPage += 1
        home()

def menu_previous_page():
    global menuCurrentPage
    if menuCurrentPage != 1:
        menuCurrentPage -= 1
        home()

def item_selected(item, price):
    if item in _basketDictionary:
        coffee = _basketDictionary[item]
        newQuantity = coffee[1] + 1
        newPrice = price * newQuantity
        _basketDictionary[item] = [newPrice, newQuantity]
        show_popup("Item Selected", f"{item} Added to basket")
        # print(_basketDictionary)
    else:
        _basketDictionary[item] = [price, 1]
        show_popup("Item Selected", f"{item} Added to basket")
    # print(_basketDictionary)

# Home screen
def home():
    remove_all_widgets(mainFrame)
    # print(_user, _password, _postcode, _mobile, _shop)

    # Title of the page
    regLabel = Label(mainFrame, text="Menu", font=header_font, background=background)
    regLabel.place(width=100, x=110, y=10)
        
    menuFrame = Frame(mainFrame, style="Main.TFrame")
    menuFrame.place(width=300, height=350, x=0, y=50)

    coffee_data = get_all_products()

    counter = 0
    pageCounter = 1
    tempPage = []
    pages = {}
    position = 0

    for num, coffee, price in coffee_data:
        # print(coffee, price)
        
        tempPage.append([coffee, price])
        counter += 1
        
        if counter % 6 == 0:
            pages[pageCounter] = list(tempPage)
            pageCounter += 1
            tempPage.clear()
    pages[pageCounter] = list(tempPage)

    menuLastPage = list(pages.keys())[-1]
    # print(menuLastPage)
    # print(pages)

    counter = 0
    for coffee, price in pages[menuCurrentPage]:
        # print(coffee, price)
        coffeeFrame = Frame(menuFrame)
        coffeeFrame.place(width=300, height=50, x=0, y=position)
        coffeeFrame.config(style="Main.TFrame")
        coffeeName = Label(coffeeFrame, text=coffee, background=background)
        coffeePrice = Label(coffeeFrame, text=f"£{price}", background=background)
        selectButton = Button(coffeeFrame, text="Select", command=lambda coffee=coffee, price=price: item_selected(coffee, price))

        counter +=1
        position += 50

        coffeeName.place(width=150, height=30, y=10, x=10)
        coffeePrice.place(width=40, height=30, y=10, x=170)
        selectButton.place(width=70, height=30, y=10, x=220)

    global menuBackButton
    global menuNextButton
    pageControlFrame = Frame(mainFrame, style="Main.TFrame")
    menuBackButton = Button(pageControlFrame, text="<--", command=menu_previous_page)
    pageLabel = Label(pageControlFrame, text=f"Page {menuCurrentPage}", background=background)
    itemAdded = Label(pageControlFrame, text="", background=background)
    menuNextButton = Button(pageControlFrame, text="-->", command=lambda: menu_next_page(menuLastPage))

    pageControlFrame.place(width=300, height=50, x=0, y=350)
    menuBackButton.place(width=70, height=30, y=10, x=18)
    pageLabel.place(width=40, height=20, y=15, x=130)
    itemAdded.place(width=100, y=35, x=100)
    menuNextButton.place(width=70, height=30, y=10, x=212)

    if menuCurrentPage == 1:
        menuBackButton.configure(state="disabled")
    else:
        menuBackButton.configure(state="normal")

    if menuCurrentPage == menuLastPage:
        menuNextButton.configure(state="disabled")
    else:
        menuNextButton.configure(state="normal")


def show_order(orderNo, user, storeID, quantities, items, prices, total):
    popup = Toplevel(root)
    popup.title(f"Order: {orderNo}")
    popup.config(background=background)

    rows = list(zip(quantities, items, prices))
    
    orderLabel = Label(popup, text=f"{orderNo}", font=small_header, background=background)
    orderLabel.pack(pady=10)

    for quantity, item, price in rows:
        Label(popup, text=f"{quantity}    {item}    {price}").pack(pady=10)

    totalLabel = Label(popup, text=f"Total: {total}", font=small_header, background=background)
    totalLabel.pack(pady=10)

    closeBtn = Button(popup, text="Close", height=2, width=10, command=popup.destroy)
    closeBtn.pack(pady=20)

    clearBtn = Button(popup, text="Clear Order", height=2, width=10, command=lambda: delete_order(orderNo))
    clearBtn.pack(pady=20)

def view_orders():
    remove_all_widgets(mainFrame)

    veiwOrderLabel = Label(mainFrame, text="Orders", font=header_font, background=background)
    veiwOrderLabel.place(width=100, x=110, y=10)

    orders = view_orders()

# Profile screen
def profile():
    remove_all_widgets(mainFrame)

    print(_shop, _shopID)

    # Labels
    regLabel = Label(mainFrame, text="Profile", font=header_font, background=background)
    userLabel = Label(mainFrame, text="Enter username: ", background=background)
    passwordLabel = Label(mainFrame, text="Enter password: ", background=background)
    postcodeLabel = Label(mainFrame, text="Enter postcode: ", background=background)
    mobileLabel = Label(mainFrame, text="Enter mobile: ", background=background)

    user = Label(mainFrame, text=_user, background=background)
    password = Label(mainFrame, text="*"*len(_password), background=background)
    postcode = Label(mainFrame, text=_postcode, background=background)
    mobile = Label(mainFrame, text=_mobile, background=background)

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
basketCurrentPage = 1
def basket_next_page(basketLastPage):
    global basketCurrentPage
    if basketCurrentPage != basketLastPage:
        basketCurrentPage += 1
        basket()

def basket_previous_page():
    global basketCurrentPage
    if basketCurrentPage != 1:
        basketCurrentPage -= 1
        basket()

def update_basket(coffee, price, quantity):
    coffeeDict = get_all_products_dictioanary()
    # print(quantity)
    coffeeInfo = coffeeDict[coffee]
    # print(coffeeInfo[1])
    newPrice = float(coffeeInfo[1]) * float(quantity)
    _basketDictionary[coffee] = [newPrice, quantity]
    show_popup("Updated Basket", "Basket updated")
    basket()

def delete_item_from_basket(item):
    _basketDictionary.pop(item)
    show_popup("Item Deleted", f"{item} deleted")
    basket()

def basket():
    remove_all_widgets(mainFrame)
    global _total
    _total = 0

    # Title of the page
    regLabel = Label(mainFrame, text="Basket", font=header_font, background=background)
    regLabel.place(width=100, x=110, y=10)

    # Basket frame
    basketFrame= Frame(mainFrame, style="Main.TFrame")
    basketFrame.place(width=300, height=300, x=0, y=50)

    # Add forloop to create the content for products
    counter = 0
    pageCounter = 1
    tempPage = []
    pages = {}
    position = 0

    for coffee in _basketDictionary:
        #print(coffee)
        
        tempPage.append([coffee])
        counter += 1
        
        if counter % 5 == 0:
            pages[pageCounter] = list(tempPage)
            pageCounter += 1
            tempPage.clear()
    pages[pageCounter] = list(tempPage)

    basketLastPage = list(pages.keys())[-1]
    #print(basketLastPage)
    #print(pages)

    counter = 0
    for product in pages[basketCurrentPage]:
        coffee = _basketDictionary[product[0]]
        price = coffee[0]
        quantity = coffee[1]
        #print(product, price, quantity)

        coffeeFrame = Frame(basketFrame)
        coffeeFrame.place(width=300, height=50, x=0, y=position)
        coffeeFrame.config(style="Main.TFrame")
        quantityEntry = Entry(coffeeFrame)
        coffeeName = Label(coffeeFrame, text=product, background=background)
        coffeePrice = Label(coffeeFrame, text=f"£{price}", background=background)
        updateButton = Button(coffeeFrame, text="update", command=lambda entry=quantityEntry, coffee=product[0], price=price: update_basket(coffee, price, entry.get()))
        binButton = Button(coffeeFrame, text="bin", command=lambda coffee=product[0]: delete_item_from_basket(coffee))
        quantityEntry.insert(END, quantity)

        counter +=1
        position += 50
        
        quantityEntry.place(width=20, height=30, y=10, x=5)
        coffeeName.place(width=130, height=30, y=10, x=30)
        coffeePrice.place(width=40, height=30, y=10, x=170)
        updateButton.place(width=70, height=20, y=3, x=220)
        binButton.place(width=70, height=20, y=28, x=220)
        

    global basketBackButton
    global basketNextButton
    pageControlFrame = Frame(mainFrame, style="Main.TFrame")
    basketBackButton = Button(pageControlFrame, text="<--", command=basket_previous_page)
    pageLabel = Label(pageControlFrame, text=f"Page {basketCurrentPage}", background=background)
    basketNextButton = Button(pageControlFrame, text="-->", command=lambda: basket_next_page(basketLastPage))

    pageControlFrame.place(width=300, height=50, x=0, y=300)
    basketBackButton.place(width=70, height=30, y=10, x=18)
    pageLabel.place(width=40, height=30, y=10, x=130)
    basketNextButton.place(width=70, height=30, y=10, x=212)

    if basketCurrentPage == 1:
        basketBackButton.configure(state="disabled")
    else:
        basketBackButton.configure(state="normal")

    if basketCurrentPage == basketLastPage:
        basketNextButton.configure(state="disabled")
    else:
        basketNextButton.configure(state="normal")

    # Checkout button
    checkoutButton = Button(mainFrame, text="checkout", command=checkout_screen)
    checkoutButton.place(width=80, height=30, x=110, y=360)

    if len(_basketDictionary) == 0:
        checkoutButton.config(state="disabled") 
    
    for product in _basketDictionary:
        _total += _basketDictionary[product][0]

    totalLabel = Label(mainFrame, text=f"Total: £{_total}", background=background)
    totalLabel.place(width=80, height=30, x=210, y=360)


checkCurrentPage = 1
def check_next_page(checkLastPage):
    global checkCurrentPage
    if checkCurrentPage != checkLastPage:
        checkCurrentPage += 1
        checkout_screen()

def check_previous_page():
    global checkCurrentPage
    if checkCurrentPage != 1:
        checkCurrentPage -= 1
        checkout_screen()

def checkout_screen():
    remove_all_widgets(mainFrame)
    
    # Title of the page
    regLabel = Label(mainFrame, text="Checkout", font=header_font, background=background)
    regLabel.place(width=120, x=90, y=10)

    # Store label
    storeLabel = Label(mainFrame, text=f"Store: {_shop}", background=background)
    storeLabel.place(width=150, x=0, y=50)

    # Item total
    storeLabel = Label(mainFrame, text=f"Total: £{_total}", background=background)
    storeLabel.place(width=120, x=180, y=50)

    # Item veiwer
    itemFrame= Frame(mainFrame, style="Main.TFrame")
    itemFrame.place(width=300, height=120, x=0, y=70)

    counter = 0
    pageCounter = 1
    tempPage = []
    pages = {}
    position = 0

    for coffee in _basketDictionary:
        #print(coffee)
        
        tempPage.append([coffee])
        counter += 1
        
        if counter % 3 == 0:
            pages[pageCounter] = list(tempPage)
            pageCounter += 1
            tempPage.clear()
    pages[pageCounter] = list(tempPage)

    checkLastPage = list(pages.keys())[-1]
    #print(basketLastPage)
    #print(pages)
    
    # Add forloop to create the content for products
    counter = 0
    for product in pages[checkCurrentPage]:
        coffee = _basketDictionary[product[0]]
        price = coffee[0]
        quantity = coffee[1]
        # print(price, quantity)

        coffeeFrame = Frame(itemFrame, style="Main.TFrame")
        coffeeFrame.place(width=300, height=50, x=0, y=position)

        quantityLabel = Label(coffeeFrame, text=quantity, background=background)
        coffeeLabel = Label(coffeeFrame, text=product, background=background)
        priceLabel = Label(coffeeFrame, text=f"£{price}", background=background)

        quantityLabel.place(width=20, height=20, y=5, x=10)
        coffeeLabel.place(width=120, height=20,y=5, x=100)
        priceLabel.place(width=50, height=20, y=5, x=250)

        position +=30

    global checkBackButton
    global checkNextButton
    pageControlFrame = Frame(itemFrame, style="Main.TFrame")
    checkBackButton = Button(pageControlFrame, text="<--", command=check_previous_page)
    pageLabel = Label(pageControlFrame, text=f"Page {basketCurrentPage}", background=background)
    checkNextButton = Button(pageControlFrame, text="-->", command=lambda: check_next_page(checkLastPage))

    pageControlFrame.place(width=300, height=30, x=0, y=90)
    checkBackButton.place(width=70, height=20, y=5, x=18)
    pageLabel.place(width=40, height=20, y=5, x=130)
    checkNextButton.place(width=70, height=20, y=5, x=212)

    if checkCurrentPage == 1:
        checkBackButton.configure(state="disabled")
    else:
        checkBackButton.configure(state="normal")

    if checkCurrentPage == checkLastPage:
        checkNextButton.configure(state="disabled")
    else:
        checkNextButton.configure(state="normal")

    # Card information
    # Labels 
    nameOnCardLabel = Label(mainFrame, text="Name on card", background=background)
    cardNumberLabel = Label(mainFrame, text="Card number", background=background)
    cvv2Label = Label(mainFrame, text="CVV2", background=background)

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
    payButton = Button(mainFrame, text="Pay", command=paying_process)
    payButton.place(width=80, height=30, x=110, y=360)


# Checkout screen
def paying_process():
    coffeeList = ""
    priceList = ""
    quantityList = ""

    lastCoffee = list(_basketDictionary.keys())[-1]
    # print(lastCoffee)

    for coffee in _basketDictionary:
        if coffee == lastCoffee:
            coffeeList += coffee
            priceList += str(_basketDictionary[coffee][0])
            quantityList += str(_basketDictionary[coffee][1])
        else:
            coffeeList += f"{coffee}, "
            priceList += f"{_basketDictionary[coffee][0]}, "
            quantityList += f"{_basketDictionary[coffee][1]}, "

    # print(coffeeList)
    # print(priceList)
    # print(quantityList)

    global _orderNumber
    _orderNumber = randint(100000, 999999)

    while check_order_id(_orderNumber):
        _orderNumber = randint(100000, 999999)

    add_order(_orderNumber, _user, _shopID, quantityList, coffeeList, priceList, _total)
    ordered_screen()


# Order screen
def leave_ordered_screen():
    homeButton.config(state="normal")
    basketButton.config(state="normal")
    profileButton.config(state="normal")
    reset_variables()
    home()

orderCurrentPage = 1
def order_next_page(orderLastPage):
    global orderCurrentPage
    if orderCurrentPage != orderLastPage:
        orderCurrentPage += 1
        ordered_screen()

def order_previous_page():
    global orderCurrentPage
    if orderCurrentPage != 1:
        orderCurrentPage -= 1
        ordered_screen()

def ordered_screen():
    remove_all_widgets(mainFrame)
    homeButton.config(state="disabled")
    basketButton.config(state="disabled")
    profileButton.config(state="disabled")

    # Title of the page
    regLabel = Label(mainFrame, text=f"Order # {_orderNumber}", font=header_font, background=background)
    regLabel.place(width=300, x=0, y=10)

    pages = {}
    orderPageCounter = 1
    itemCounter = 0
    pageContent = []
    yposition = 50
    #print(_basketDictionary)

    for product in _basketDictionary:

        pageContent.append([product])
        itemCounter += 1

        #print(product)
        if itemCounter %5 == 0:
            pages[orderPageCounter] = list(pageContent)
            pageContent = []
            orderPageCounter +=1
        
        pages[orderPageCounter] = list(pageContent)
    
    itemCounter = 0
    for item in pages[orderCurrentPage]:
        coffee = _basketDictionary[product]
        price = coffee[0]
        quantity = coffee[1]
        #print(price, quantity)
        
        coffeeFrame = Frame(mainFrame, style="Main.TFrame")
        coffeeFrame.place(width=300, height=50, x=0, y=yposition)
        yposition += 50

        coffeeLabel = Label(coffeeFrame, text=item, background=background)
        priceLabel = Label(coffeeFrame, text=f"£{price}", background=background)
        quantityLabel = Label(coffeeFrame, text=quantity, background=background)

        quantityLabel.place(width=40, height=30, y=10, x=20)
        coffeeLabel.place(width=120, height=30, y=10, x=100)
        priceLabel.place(width=60, height=30, y=10, x=240)

    global orderBackButton
    global orderNextButton
    pageControlFrame = Frame(mainFrame, style="Main.TFrame")
    orderBackButton = Button(pageControlFrame, text="<--", command=order_previous_page)
    pageLabel = Label(pageControlFrame, text=f"Page {orderCurrentPage}", background=background)
    orderNextButton = Button(pageControlFrame, text="-->", command=lambda: order_next_page(orderPageCounter))

    pageControlFrame.place(width=350, height=50, x=0, y=350)
    orderBackButton.place(width=70, height=30, y=10, x=18)
    pageLabel.place(width=40, height=30, y=10, x=130)
    orderNextButton.place(width=70, height=30, y=10, x=212)

    if orderCurrentPage == 1:
        orderBackButton.configure(state="disabled")
    else:
        orderBackButton.configure(state="normal")

    if orderCurrentPage == orderPageCounter:
        orderNextButton.configure(state="disabled")
    else:
        orderNextButton.configure(state="normal")

    totalLabel = Label(mainFrame, text="Total:", font=header_font, background=background)
    totalLabel.place(width=100, x=0, y=320)

    newHomeButton = Button(mainFrame, text="Return Home", command=leave_ordered_screen)
    newHomeButton.place(width=80, height=30, x=110, y=320)
   
    costLabel = Label(mainFrame, text=f"£{_total}", font=header_font, background=background)
    costLabel.place(width=100, x=200, y=320)

if __name__ == "__main__":
    starter_screen()