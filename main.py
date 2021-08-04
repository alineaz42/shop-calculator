
print("************ Wellcome to Neo Shop ************")
priceAndValue = {}
total = 0
while True:
    productName = input("Enter the name of the product \n")

    if productName != "q":
        try:
            productPrice = int(input("Enter price of the product \n"))
            priceAndValue.update({productName: productPrice})

        except ValueError as e:
            print("Make sure you enter a number")
    elif productName == "q":
        for key, values in priceAndValue.items():
            print(f"{key} = {values} ")

        l = [i for i in priceAndValue.values()]
        total = sum(l)

        print(f"The total is {total}")

        with open("recipt.txt", "w") as f:
            f.write(str(priceAndValue))

        break
    elif productName == "e":
        exit()
