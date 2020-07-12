op=open('/Users/anujsrivastav/Downloads/text.txt','r')
count=0

for line in op:
    count=count+1
    print(count,line.rstrip())
#File pointer has reached at the end of the file so read do not have anything to read.
re=op.read()
print("\nPrint Content of Read\n")
for line in re:
    print(re[:])
#To overcome this we either again need to read the file or set the file pointer to 0.
op.seek(0)
re=op.read()
print("\nRe-attempting to Print Content of Read\n")
print(re[:])

