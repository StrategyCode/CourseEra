TotVal = 0
NumberOfLines = 0
FileName = input("Enter the File Name to read: ")
try:
    FileHandle = open(FileName,'r')
except:
    print("File provided does not exist. Please provide valid file name.")
    exit()
for line in FileHandle:
    if line.startswith("X-DSPAM-Confidence:"):
        FlVal = float(line.split(":")[1].strip())
        TotVal = TotVal + FlVal
        NumberOfLines = NumberOfLines + 1
print("Average spam confidence:",TotVal/NumberOfLines)