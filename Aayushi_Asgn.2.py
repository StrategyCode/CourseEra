Day=input().rstrip()
Hour=int(input().rstrip())
MinGMT=int(input().rstrip())
WeekDays=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if ((Hour > 0 and Hour < 24) and (MinGMT > 0 and MinGMT < 60)):
    if (MinGMT + 30) > 60:
        MinIST=MinGMT + 30 - 60
        Hour=Hour+1
    elif (MinGMT + 30) == 60:
        MinIST=00
        Hour=Hour+1
    else:
        MinIST=MinGMT +30
    if (Hour + 5) >24:
        HourIST=Hour + 5 - 24
        if WeekDays.index(Day) == 6:
            DayIST=WeekDays[0]
        else:
            DayIST = WeekDays[WeekDays.index(Day) + 1]
    else:
        HourIST=Hour + 5
        DayIST=Day
    print(DayIST)
    print(HourIST)
    print(MinIST)