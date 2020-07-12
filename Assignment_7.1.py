FileName = input("Enter the File Name to Read: ")
try:
    FileHandle = open(FileName,'r')
except:
    print("File Name provided doest not exist. Please provide valid file name.")
    exit()
for line in FileHandle:
    print(line.upper().rstrip())
