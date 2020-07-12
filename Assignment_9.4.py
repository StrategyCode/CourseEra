# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
Sender=dict()
MaxMailCount=None
MaxMailFromSender=None
try:
    FileHandle=open("/Users/anujsrivastav/Downloads/mbox-short.txt","r")
except:
    print("File provided is not present.")
    exit()

#For creating the histogram of the number of mail sent by Sender

for line in FileHandle:
    if line.startswith("From "):
        Sender[line.rstrip().split()[1]]=Sender.get(line.rstrip().split()[1],0) + 1

#For getting the max number of mail sent by any sender

for key,value in Sender.items():
    if MaxMailCount is None or MaxMailCount < value:
        MaxMailCount=value
        MaxMailFromSender=key
print(MaxMailFromSender,MaxMailCount)
