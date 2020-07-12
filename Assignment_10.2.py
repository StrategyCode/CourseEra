# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
Hour=dict()
Container=list()
FileName=input("Enter the File name: ")
if len(FileName) < 1 :
    FileName="mbox-short.txt"
FileHandle=open(FileName,'r')

#Created the Histogram for the Hour and its count

for line in FileHandle:
    if line.rstrip().startswith("From "):
        Hour[line.rstrip().split(":")[0].split()[5]]=Hour.get(line.rstrip().split(":")[0].split()[5],0) + 1

#Creating Tuple of Key and Value and sorting it based on key.

for k,v in Hour.items():
    Container.append((k,v))

#Printing the final content in Required format

for i in sorted(Container):
    print(i[0],i[1])