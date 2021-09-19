'''github
origin:https://github.com/alineaz42/shop-calculator/commits/main
pushed
'''

print("welcome to future:")


def calc(name, address):
    bazarList = {}
    total = 0
    while True:
        productName = input("Enter product name or q to quite: ")
        if productName != "q":
            try:
                price = int(input("Enter the price of the productd: "))
                bazarList.update({productName: price})
            except ValueError as e:
                print("make sure enter the right price")
        elif productName == "q":
            for key, value in bazarList.items():
                print(f"{key} = {value}")
            l = [i for i in bazarList.values()]
            total = sum(l)
            print(f"The total is: {total}")
            print(f"Thank you Mr. {name},{address} \n for shoping with us")
            break


name = input("Enter Your Name: ")
address = input("Enter Your Address: ")

a = calc(name, address)
