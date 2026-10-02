patients = {"Rhea":(105,130,400),
            "Alex":(80,90,100)}

normal = 120
for pn , bs in patients.items():
    if (pn == "Rhea"):
        print("Rhea")
        print("Blood Sugar Summary")
        for value in bs:
            if value < 120:
                print(value, "not formal")
            else:
                print(value, "not normal")


        highest = max(bs)
        print("Highest Blood Sugar Count:", highest)
        lowest = min(bs)
        print(lowest, bs)
        diff = highest - lowest
        print(diff)
