count = 0
try:
    FileName = open("/Users/anujsrivastav/Downloads/mbox-short.txt","r")
except:
    print("Please provide the correct file name.")
    exit()
for line in FileName:
    if line.startswith("From "):
        # if line.startswith("From:"):
        #     continue
        print(line.rstrip().split()[1])
        count = count + 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")