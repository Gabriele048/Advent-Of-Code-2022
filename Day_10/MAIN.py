import math
inputFile= open("input.txt", "r")
operation = []
cycleNumber = 1
X = 1
for line in inputFile:
    line = line.strip().split(" ")
    nCycleToExit = line[0]   
    if(nCycleToExit == "addx"):
        operation.append((cycleNumber, X))
        cycleNumber+=1      
        operation.append((cycleNumber, X))
        X += int(line[1])
        cycleNumber += 1
    else:
        operation.append((cycleNumber, X))
        cycleNumber += 1
matches = [20, 60, 100, 140, 180, 220]
sum=0
for o in range(len(operation)):
    if(operation[o][0] in matches):
        sum += operation[o][0]*operation[o][1]
print(sum)

#PART2
screen = [["." for y in range(40)] for x in range(6)]

for o in range(len(operation)):
    CRT_pos = (operation[o][0]-1) % 40
    line = math.floor((operation[o][0]-1)/40)
    #print(CRT_pos, "\t", line)
    if(operation[o][1]-1 <= CRT_pos <= operation[o][1]+1):
        screen[line][CRT_pos] = "#"

for x in screen:
    for c in x:
        print(c, end = "")
    print()


inputFile.close()