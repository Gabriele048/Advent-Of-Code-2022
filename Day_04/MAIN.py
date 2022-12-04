# # #PART1

# inputFile= open("input.txt", "r")

# def areFullyContain (elf1, elf2):
#     if((elf1[0]>=elf2[0] and elf1[1]<=elf2[1]) or (elf1[0]<=elf2[0] and elf1[1]>=elf2[1])):
#         return True
#     else:
#         return False
# counter=0
# for line in inputFile:
#     line=line.strip().split(",")
#     elf1=(int(line[0].split("-")[0]),int(line[0].split("-")[1]))
#     elf2=(int(line[1].split("-")[0]),int(line[1].split("-")[1]))
#     if areFullyContain(elf1, elf2):
#         counter+=1  
# print(counter) 
# inputFile.close()

# #PART1

inputFile= open("input.txt", "r")

def doOverlap (elf1, elf2):
    if((elf1[0]>=elf2[0] and elf1[1]<=elf2[1]) or (elf1[0]<=elf2[0] and elf1[1]>=elf2[1])):
        return True
    elif((elf2[0]<=elf1[0]<=elf2[1] and elf1[1]>=elf2[1])or(elf1[0]<=elf2[0]<=elf1[1] and elf2[1]>=elf1[1])):
        return True
    else:
        return False
counter=0
for line in inputFile:
    line=line.strip().split(",")
    elf1=(int(line[0].split("-")[0]),int(line[0].split("-")[1]))
    elf2=(int(line[1].split("-")[0]),int(line[1].split("-")[1]))
    if doOverlap(elf1, elf2):
        counter+=1  
print(counter) 
inputFile.close()