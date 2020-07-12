def computepay():
    if Hr > 40:
        GrossPay=((Hr-40) * 1.5 * RatePerHour + (40 * RatePerHour))
    else:
        GrossPay=Hr * RatePerHour
    return GrossPay
Hr=input("Enter Hours Worked")
RatePerHour=input("Enter Rate per Hours")
try:
    Hr=float(Hr)
    RatePerHour=float(RatePerHour)
except:
    print("Please enter valid entry")
    exit()
print(computepay())
#print(NetGrossPay)