noHour = float(input("Work Hours: "))
choice = int(input("1] JANITOR:  2] CLERK: "))
position = ""
salary = 0
if choice == 1:
    position = "JANITOR"
    salary = 10000

if choice == 2:
    position = "CLERK"
    salary = 20000

else:
    print("invalid")

halfMonth = salary / 88
ratepehour = halfMonth / 88
absenceded = 0
netsalary = 0

if noHour >= 88:
    extraHours = noHour - 88
    otRate = ratepehour * 1.25
    overTimepay = otRate * extraHours
    netsalary = halfMonth + overTimepay
    print("Overtime Pay: ", overTimepay )

elif noHour <= 88:
    absence = 88 - noHour
    obsencended = ratepehour * 1.10 * absence
    netsalary = halfMonth - absenceded
    print(f"absence debutetion {absenceded:,.2f}")

else:
    print("invalid")

print(f"Net Salary:  {netsalary:,.2f}")
print("Position", position)
