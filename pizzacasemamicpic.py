MamicpicFlavor = input("Enter pizza flavor (Hawaiian/Pepperoni/Cheese): ").lower()

match MamicpicFlavor:
    case "hawaiian":
        print("You Selected Hawaiian")

        MamicpicSize = input("Enter size (Small/Medium/Large): ").lower()

        match MamicpicSize:
            case "small":
                MamicpicPrice = 250
            case "medium":
                MamicpicPrice = 350
            case "large":
                MamicpicPrice = 450
            case _:
                MamicpicPrice = 0
                print("Invalid Size")

    case "pepperoni":
        print("You Selected Pepperoni")

        MamicpicSize = input("Enter size (Small/Medium/Large): ").lower()

        match MamicpicSize:
            case "small":
                MamicpicPrice = 350
            case "medium":
                MamicpicPrice = 550
            case "large":
                MamicpicPrice = 1000
            case _:
                MamicpicPrice = 0
                print("Invalid Size")

    case "cheese":
        print("You Selected Cheese")

        MamicpicSize = input("Enter size (Small/Medium/Large): ").lower()

        match MamicpicSize:
            case "small":
                MamicpicPrice = 200
            case "medium":
                MamicpicPrice = 400
            case "large":
                MamicpicPrice = 550
            case _:
                MamicpicPrice = 0
                print("Invalid Size")

    case _:
        MamicpicPrice = 0
        print("Invalid pizza flavor.")

if MamicpicPrice > 0:
    print("Pizza Price:", MamicpicPrice)
