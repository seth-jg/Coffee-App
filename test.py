cof = {"coffee1": [1,2], "coffee2": [3,4], "coffee3": [5,6], "coffee4": [7,8], "coffee5": [9,1]}

coffeeList = ""
priceList = ""
quantityList = ""

lastCoffee = list(cof.keys())[-1]
print(lastCoffee)

for coffee in cof:
    if coffee == lastCoffee:
        coffeeList += coffee
        priceList += str(cof[coffee][0])
        quantityList += str(cof[coffee][1])
    else:
        coffeeList += f"{coffee}, "
        priceList += f"{cof[coffee][0]}, "
        quantityList += f"{cof[coffee][1]}, "

print(coffeeList)
print(priceList)
print(quantityList)