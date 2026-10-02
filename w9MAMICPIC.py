MAMICPICSeconds = float(input("Input Amount of Seconds you want to Convert: "))

MAMICPICMinutes = MAMICPICSeconds / 60
MAMICPICHours = MAMICPICSeconds / 3600
MAMICPICDays = MAMICPICSeconds / 86400
MAMICPICWeeks = MAMICPICSeconds / 604800
MAMICPICMonths = MAMICPICSeconds / 2628000
MAMICPICYears = MAMICPICSeconds / 31540000

print(f"Seconds: {MAMICPICSeconds:.2f}")

print(f"Minutes: {MAMICPICMinutes:.2f}")
print("Hours: ",MAMICPICHours)
print("Days: ",MAMICPICDays)
print("Weeks: ",MAMICPICWeeks)
print("Months: ",MAMICPICMonths)
print("Years: ",MAMICPICYears)
