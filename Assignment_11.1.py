import re
sum=0
FileHandle=open('/Users/anujsrivastav/Downloads/regex_sum_262653.txt','r')
NumList=re.findall('[0-9]+',FileHandle.read())
for num in NumList:
    sum=sum + int(num)
print(sum)