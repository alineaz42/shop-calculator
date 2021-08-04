

priceAndValue = {}

while True:
    print("Enter the item price or q to quit or e to exit : \n")
    productName = input("Enter the name of the product \n")
    productPrice = input("Enter price of the product \n")
    if productName != "q":
        try:
            priceAndValue.update({productName: productPrice})

        except ValueError as e:
            print("Make sure you enter a number")
    elif productName == "q":
        for item in priceAndValue.keys():
            for price in priceAndValue.values():
                print(f"{item} = {price}")
        break
# elif productName == "q":
#     print(f"Your total bill is {priceAndValue} ")
#     print("Thanks for shoping with us!")
# elif productName == "e":
