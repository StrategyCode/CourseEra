entry="start"
MaxNum=None
MinNum=None
while entry != "Done":
    entry=input("Enter an integer number")
    try:
        num=int(entry)
    except:
        if entry != "Done":
            print("Invalid input")
        continue
    if MaxNum is None:
        MaxNum = num
    elif MaxNum < num:
        MaxNum =num
    if MinNum is None:
        MinNum=num
    elif MinNum > num:
        MinNum=num
print("Maximum is",MaxNum)
print("Minimum is",MinNum)