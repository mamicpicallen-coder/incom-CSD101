MamicpicFlavor = input("Enter pizza flavor (Hawaiian/Pepperoni/Cheese): ").lower()

if MamicpicFlavor == "hawaiian":
    print("You Selected Hawaiian")

    MamicpicSize = input("Enter size (Small/Medium/Large): ").lower()

    if MamicpicSize == "small":
        MamicpicPrice = 250
    elif MamicpicSize == "medium":
        MamicpicPrice = 350
    elif MamicpicSize == "large":
        MamicpicPrice = 450
    else:

        price = 0
        print("Invalid Size")

elif MamicpicFlavor == "pepperoni":
    print("You Selected Pepperoni")

    MamicpicSize = input("Enter size (Small/Medium/Large): ").lower()

    if MamicpicSize == "small":
        MamicpicPrice = 350
    elif MamicpicSize == "medium":
        MamicpicPrice = 550
    elif MamicpicSize == "large":
        MamicpicPrice = 1000
    else:
        price = 0
        print("Invalid Size")

elif MamicpicFlavor == "cheese":
    print("You Selected Cheese")

    MamicpicSize = input("Enter size (Small/Medium/Large): ").lower()

    if MamicpicSize == "small":
        MamicpicPrice = 200
    elif MamicpicSize == "medium":
        MamicpicPrice = 400
    elif MamicpicSize == "large":
        MamicpicPrice = 550
    else:
        MamicpicPrice = 0
        print("Invalid Size")
else:
    MamicpicPrice = 0
    print("Invalid pizza flavor.")
if MamicpicPrice > 0:
    print("Pizza Price: ", MamicpicPrice)
