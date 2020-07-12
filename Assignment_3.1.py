hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    h=45
RatePerHour=input("Enter Rate Per Hour:")
try:
    r=float(RatePerHour)
except:
    r=10.50
if h <= 40:
    GrossPay=h*r
    print(GrossPay)
else:
    GrossPay=(40*r)+((h-40)*r*1.5)
    print(GrossPay)