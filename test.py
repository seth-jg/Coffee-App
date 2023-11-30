from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x500")
root.resizable(False, False)

coffee_data = [
    ["Espresso", 2.50],
    ["Americano", 3.00],
    ["Latte", 4.50],
    ["Cappuccino", 4.00],
    ["Macchiato", 3.50],
    ["Mocha", 5.00],
    ["Flat White", 4.75],
    ["Turkish Coffee", 3.75],
    ["Cold Brew", 4.25],
    ["French Press", 4.50],
    ["Affogato", 4.25],
    ["Irish Coffee", 5.50],
    ["Café au Lait", 3.25],
    ["Ristretto", 3.00],
    ["Café Cubano", 3.50],
    ["Red Eye", 3.75],
    ["Affogato", 4.25],
    ["Iced Latte", 4.50],
    ["Café con Leche", 3.75],
    ["Caramel Macchiato", 5.25],
    ["Vienna Coffee", 4.00],
    ["Café Latte", 4.25],
    ["Double Espresso", 3.50],
    ["Flat Black", 3.75],
    ["Café Americano", 3.25],
    ["Turbo Shot", 4.50],
    ["Café Miel", 4.75],
    ["Café Breve", 4.25],
    ["Iced Mocha", 5.50],
    ["Pumpkin Spice Latte", 5.25],
]

background =  "#c69f6c"
itemColor = "#D2B48C"
root.config(bg="blue")

mainStyle = Style()
nBarStyle = Style()
itemStyle = Style()

mainStyle.configure("Main.TFrame", background=background)
nBarStyle.configure("NavBar.TFrame", background="red")
itemStyle.configure("item.TFrame", background=itemColor) 

menuFrame = Frame(root, style="Main.TFrame")
menuFrame.place(width=300, height=400, x=0, y=50)

counter = 0
position = 0
for coffee, price in coffee_data:
    print(coffee, price)
    coffeeFrame = Frame(menuFrame, style="item.TFrame" if counter%2==0 else "main.TFrame")
    coffeeFrame.place(width=300, height=50, x=0, y=position)

    coffeeName = Label(coffeeFrame, text=coffee)
    coffeePrice = Label(coffeeFrame, text=price)
    selectButton = Button(coffeeFrame, text="Select")


    counter += 1
    position +=50

root.mainloop()