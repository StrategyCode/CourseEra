#Getting String User input
MasterString=input()
KangarooString=input()
KangarooStrLen=len(KangarooString)

#Default Assignment
count=0
mindex=-1

#Loop on Kanagroo String
for kstring in KangarooString:

    #Loop on Master String
    for mstring in range(mindex+1,len(MasterString)):
        if MasterString[mstring] == kstring:
            count=count+1
            mindex=MasterString.index(kstring)
            break
        else:
            continue

#Length Match
if count == KangarooStrLen:
    print('True')
else:
    print('False')