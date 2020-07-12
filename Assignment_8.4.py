FinalOutput = list()
try:
    FileName = open("/Users/anujsrivastav/Downloads/romeo.txt","r")
except:
    print("Please provide the correct file name.")
    exit()
for line in FileName:
        # Using split i.e. line.split() to convert content of line into list
        for num in range(len(line.rstrip().split())):
            if line.rstrip().split()[num] in FinalOutput:
                continue
            else:
                # Appending the word in the list if not getting repeated.
                FinalOutput.append(line.rstrip().split()[num])
print(sorted(FinalOutput))
