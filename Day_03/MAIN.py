# #PART1

# def delRepetitions(stringWithRepetition):
#     stringNoRep=""
#     for c in stringWithRepetition:
#         if stringNoRep.find(c)==-1:
#             stringNoRep+=c
#     return stringNoRep

# inputFile= open("input.txt", "r")
# errors=[]
# prioritySum=0
# for line in inputFile:
#     line=line.strip()
#     part1=line[0:int(len(line)/2)]
#     part1=delRepetitions(part1)
#     part2=line[int(len(line)/2):int(len(line))]
#     part2=delRepetitions(part2)
#     for c in part1:
#         index=part2.find(c)
#         if index>=0:
#             errors.append(part2[index])
# for c in errors:
#     if(c.islower()):
#         prioritySum += ord(c) - 96
#     else:
#         prioritySum += ord(c) - 38
##     print(c + "\t"+ str(prioritySum))
# print(prioritySum)
# inputFile.close()

#PART2

def delRepetitions(stringWithRepetition):
    stringNoRep=""
    for c in stringWithRepetition:
        if stringNoRep.find(c)==-1:
            stringNoRep+=c
    return stringNoRep

def find3Repetions(stringWithRepetition):
    for c in stringWithRepetition:
        if stringWithRepetition.count(c)==3:
            return c

inputFile= open("input.txt", "r")
badges=[]
prioritySum=0
i=0
buffer=""
for line in inputFile:
    if(i<3):
        buffer += delRepetitions(line.strip())
        i += 1
    if(i==3):
        badges.append(find3Repetions(buffer))
        #print(find3Repetions(buffer))
        buffer=""
        i=0  

for c in badges:
    if(c.islower()):
        prioritySum += ord(c) - 96
    else:
        prioritySum += ord(c) - 38
    #print(c + "\t"+ str(prioritySum))
print(prioritySum)
inputFile.close()
