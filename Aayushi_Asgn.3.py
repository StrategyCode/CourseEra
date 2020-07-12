NumberOfIteration=int(input())
TriagularSequence=list()
NumberofValues=0
loop=-1
sum=0
TrianglePath=list()

#For Calculating Number of Entries in Triangular Pattern
for i in range(1,NumberOfIteration+1):
    NumberofValues=NumberofValues+i

#Taking User Entry for Triangular Pattern
for num in range(NumberofValues):
    UserVal=int(input())
    TriagularSequence.append(UserVal)

#Creating The Triagule using List
for j in range(1,NumberOfIteration+1):
    TempList = list()
    for k in range(j):
        loop=loop+1
        TempList.append(TriagularSequence[loop])
    TrianglePath.append(TempList)

#Extracting the Maximum Sum
for l in TrianglePath:
    sum=sum+sorted(l)[-1]

print(sum)