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
    cur.execute("SELECT location FROM storeLocations")
    locations = [row[0] for row in cur.fetchall()]
    conn.close()
    return locations


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