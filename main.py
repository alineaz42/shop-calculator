

sum = 0
while True:
    userInput = input("Enter the item price or q to quit : \n")
    if userInput != "q":
        sum = sum+int(userInput)
        print(f"order total so far {sum}")

    else:
        print(f"Your total bill is {sum} ")
        print("Thanks for showping with us!")
        break
