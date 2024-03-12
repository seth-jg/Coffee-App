import sqlite3
from tkinter import *

def delete_order(orderID):
        conn = sqlite3.connect("BeansAndBrewDatabase.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM orders WHERE orderID=?", (orderID,))
        conn.commit()
        conn.close()

def veiw_orders():
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    conn.close()
    return orders

# print(len(veiw_orders()))
# [(Order number, username, storeID, all quantities, all items, all prices, total), (repeat)]
# [(937387, 'seth', 3, '1, 1, 1, 1, 1, 1, 1, 1, 1, 1', 'Espresso, Americano, Latte, Cappuccino, Macchiato, Mocha, Flat White, Turkish Coffee, Cold Brew, French Press', '2.5, 3.0, 4.5, 4.0, 3.5, 5.0, 4.75, 3.75, 4.25, 4.5', 39.75)]
# print(veiw_orders())


from faker import Faker
fake = Faker()

print(fake.name())