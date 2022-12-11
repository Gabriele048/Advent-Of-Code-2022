# #PART1
# inputFile= open("input.txt", "r")
# grid = []
# for line in inputFile:
#     line = line.strip()
#     row = []
#     for c in line:
#         row.append(int(c))
#     grid.append(row)

# # at least the perimeter 
# visibleTree = 2 * len(grid) + 2 * len(grid[0]) - 4
# #list of coordinates of visible tree. At the and there would be some doubled elements
# coordList = []

# #up POV
# for x in range(1,len(grid[0])-1):
#     max = grid[0][x]
#     for y in range(1,len(grid)-1):
#         if (grid[y][x] > max):
#             max = grid[y][x]
#             coordList.append((x,y))       
# #down POV
# for x in range(1,len(grid[0])-1):
#     max = grid[len(grid)-1][x]
#     for y in range(len(grid)-2, 0, -1):
#         if (grid[y][x] > max):
#             max = grid[y][x]
#             coordList.append((x,y))    
# #right POV
# for y in range(1,len(grid)-1):
#     max = grid[y][len(grid[0])-1]
#     for x in range(len(grid[0])-2, 0, -1):
#         if (grid[y][x] > max):
#             max = grid[y][x]
#             coordList.append((x,y)) 
# #left POV
# for y in range(1,len(grid)-1):
#     max = grid[y][0]
#     for x in range(1, len(grid[0])-1):
#         if (grid[y][x] > max):
#             max = grid[y][x]
#             coordList.append((x,y)) 
# print(len(coordList))

# notDoubledList = [] 

# for c in coordList:
#     if not(c in notDoubledList):
#         notDoubledList.append(c)
# visibleTree+=len(notDoubledList)
# print(visibleTree)
# inputFile.close()

#PART2
inputFile= open("input.txt", "r")
grid = []
for line in inputFile:
    line = line.strip()
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row)

scoreMatrix = [[1 for x in range(len(grid[0]))] for y in range(len(grid))]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        score = 1
        if(x < (len(grid[0])-1)):#turn right
            tempScore = 0
            for r in range(x+1, len(grid[0])):
                max = grid[y][x]
                if grid[y][r] >= grid[y][x]:
                    tempScore +=1
                    break
                else:
                    tempScore +=1
            score*=tempScore
        else:
            score = 0
        if(x > 0):#turn left
            tempScore = 0
            for l in range(x-1, -1, -1):
                max = grid[y][x]
                if grid[y][l] >= grid[y][x]:
                    tempScore +=1
                    break
                else:
                    tempScore +=1
            score*=tempScore
        else:
            score = 0
        if(y < (len(grid)-1)):#turn down
            tempScore = 0
            for d in range(y+1, len(grid)):
                max = grid[y][x]
                if grid[d][x] >= grid[y][x]:
                    tempScore +=1
                    break
                else:
                    tempScore +=1
            score*=tempScore
        else:
            score = 0
        if(y > 0):#turn up
            tempScore = 0
            for u in range(y-1, -1, -1):
                max = grid[y][x]
                if grid[u][x] >= grid[y][x]:
                    tempScore +=1
                    break
                else:
                    tempScore +=1
            score*=tempScore
        else:
            score = 0
        
        scoreMatrix[y][x]=score

max = 0
for row in scoreMatrix:
    for score in row:
        if score > max:
            max = score 

print(max)
       

inputFile.close()