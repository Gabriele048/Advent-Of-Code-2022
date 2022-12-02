'''
#PART1
inputFile= open("input.txt", "r")
sum=0
Calories=[]
for line in inputFile:
    line=line.splitlines(keepends=False)
    if line[0]=="":
        #print(sum)
        Calories.append(sum)
        sum=0
    else:
        sum+=int(line[0])
print(max(Calories))
inputFile.close()
'''

#PART2
inputFile= open("input.txt", "r")
sum=0
Calories=[]
for line in inputFile:
    line=line.splitlines(keepends=False)
    if line[0]=="":
        #print(sum)
        Calories.append(sum)
        sum=0
    else:
        sum+=int(line[0])
backups=3
counter=0
for i in range(0, backups):
    m=max(Calories)
    counter+=m
    Calories.remove(m)
print(counter)
inputFile.close()