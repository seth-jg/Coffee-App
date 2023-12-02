from tkinter import *
from tkinter.ttk import *
from DatabaseFunctions import * 

root = Tk()
root.geometry("300x500")
root.resizable(False, False)



background =  "#c69f6c"
itemColor = "#D2B48C"
root.config(bg="blue")

mainStyle = Style()
nBarStyle = Style()
itemStyle = Style()

mainStyle.configure("Main.TFrame", background=background)
nBarStyle.configure("NavBar.TFrame", background="red")
itemStyle.configure("item.TFrame", background=itemColor) 

mainFrame = Frame(root, style="Main.TFrame")
mainFrame.place(width=300, height=400, x=0, y=50)

basketCurrentPage = 1
def basket_next_page(basketLastPage):
    global basketCurrentPage
    if basketCurrentPage != basketLastPage:
        basketCurrentPage += 1
        home()

def basket_previous_page():
    global basketCurrentPage
    if basketCurrentPage != 1:
        basketCurrentPage -= 1
        home()

def home():

    # Title of the page
    regLabel = Label(mainFrame, text="basket")
    regLabel.place(width=100, x=110, y=10)
        
    basketFrame = Frame(mainFrame, style="Main.TFrame")
    basketFrame.place(width=300, height=300, x=0, y=50)

    _basketDictionary = {"coffee1": [2.3, 3], "coffee2": [4, 5], "coffee3": [4, 1]}

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
        print(price, quantity)

        coffeeFrame = Frame(basketFrame)
        coffeeFrame.place(width=300, height=50, x=0, y=position)
        coffeeFrame.config(style="item.TFrame" if counter % 2 == 0 else "Main.TFrame")
        quantityEntry = Entry(coffeeFrame)
        coffeeName = Label(coffeeFrame, text=coffee)
        coffeePrice = Label(coffeeFrame, text=f"£{price}")
        updateButton = Button(coffeeFrame, text="update")
        binButton = Button(coffeeFrame, text="bin")
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
    pageControlFrame = Frame(mainFrame)
    basketBackButton = Button(pageControlFrame, text="<--", command=basket_previous_page)
    pageLabel = Label(pageControlFrame, text=f"Page {basketCurrentPage}")
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
print(get_all_products())