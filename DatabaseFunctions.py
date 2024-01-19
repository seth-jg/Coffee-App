import sqlite3

def check_username_exists(username):
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM account WHERE username=?", (username,))
    result = cur.fetchone()
    conn.close()
    return result is not None


def get_all_store_locations():
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM storeLocations")
    locations = cur.fetchall()
    conn.close()
    return locations
# print(get_all_store_locations())

def check_order_id(id):
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders WHERE orderID=?", (id,))
    result = cur.fetchone()
    conn.close()
    return result is not None

def check_credentials(username, password):
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM account WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result is not None, result

# uses check credentials to return none or an array of the users info
def get_user_info(username, password):
    credentials_valid, user_row = check_credentials(username, password)
    if credentials_valid:
        return user_row
    else:
        return None

def create_new_user(username, password, postcode, mobile):
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO account (username, password, postcode, mobile) VALUES (?, ?, ?, ?)", (username, password, postcode, mobile))
    conn.commit()
    conn.close()

def add_order(id, user, storeid, quantities, items, prices, total):
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (orderID, username, storeID, quantities, items, prices, total) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, user, storeid, quantities, items, prices, total))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT productID, productName, price FROM products")
    products = cur.fetchall()
    conn.close()
    return products

def get_all_products_dictioanary():
    conn = sqlite3.connect("BeansAndBrewDatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT productID, productName, price FROM products")
    products = cur.fetchall()
    conn.close()

    coffee_dict = {}
    for product_id, coffee_name, price in products:
        coffee_dict[coffee_name] = [product_id, price]

    return coffee_dict


def delete_order(orderID):
        conn = sqlite3.connect("BeansAndBrewDatabase.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM orders WHERE orderID=?", (orderID,))
        conn.commit()
        conn.close()

def view_orders_from_database():
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