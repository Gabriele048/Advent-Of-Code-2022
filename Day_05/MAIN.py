# #PART1
# import queue
# inputFile= open("input.txt", "r")

# index=1
# stackFinishIndex=8
# moveStartIndex=11
# stacks = [[None for y in range(stackFinishIndex)] for x in range(9)]
# LIFOs=[queue.LifoQueue(maxsize=72) for x in range(9)]
# #READ STACKS
# for line in inputFile:
#     if(index<=stackFinishIndex):
#         line=line.split("\n")[0]
#         for i in range(1,34,4):
#             if(line[i]!= " "):
#                 stacks[int((i-1)/4)][index-1]=line[i]
#     elif (index==stackFinishIndex+1):
#         #ORGANIZE STACKS AS LIFO
#         for x in range(len(stacks)):
#             for i in range((len(stacks[x])-1), -1, -1):
#                 if stacks[x][i] != None:
#                     LIFOs[x].put(stacks[x][i])
#     elif (index>=moveStartIndex):
#         line=line.strip().split(" ")
#         numberOfMove=int(line[1])
#         stackFrom=int(line[3])-1
#         stackTo=int(line[5])-1
#         #print(numberOfMove,stackFrom,stackTo)
#         for i in range(numberOfMove):
#             LIFOs[stackTo].put(LIFOs[stackFrom].get())
#     index+=1
# for LIFO in LIFOs:
#     print(LIFO.get(), end=" ")
# print()

# inputFile.close()

#PART2
import queue
inputFile= open("input.txt", "r")

index=1
stackFinishIndex=8
moveStartIndex=11
stacks = [[None for y in range(stackFinishIndex)] for x in range(9)]
LIFOs=[queue.LifoQueue(maxsize=72) for x in range(9)]
#READ STACKS
for line in inputFile:
    if(index<=stackFinishIndex):
        line=line.split("\n")[0]
        for i in range(1,34,4):
            if(line[i]!= " "):
                stacks[int((i-1)/4)][index-1]=line[i]
    elif (index==stackFinishIndex+1):
        #ORGANIZE STACKS AS LIFO
        for x in range(len(stacks)):
            for i in range((len(stacks[x])-1), -1, -1):
                if stacks[x][i] != None:
                    LIFOs[x].put(stacks[x][i])
    elif (index>=moveStartIndex):
        line=line.strip().split(" ")
        numberOfMove=int(line[1])
        stackFrom=int(line[3])-1
        stackTo=int(line[5])-1
        #print(numberOfMove,stackFrom,stackTo)
        stagingTempFifo=queue.LifoQueue(maxsize=72)
        for i in range(numberOfMove):
            stagingTempFifo.put(LIFOs[stackFrom].get())
        for i in range(numberOfMove):
            LIFOs[stackTo].put(stagingTempFifo.get())
    index+=1
for LIFO in LIFOs:
    print(LIFO.get(), end=" ")
print()

inputFile.close()