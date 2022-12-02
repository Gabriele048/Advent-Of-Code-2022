# #PART1
#
# inputFile= open("input.txt", "r")
# score=0
# for line in inputFile:
#     line=line.strip().split(" ")
#     me=line[1]
#     opp=line[0]
#     if(me=="X"):
#         if(opp=="A"):
#             score+=4 ##AX
#         elif(opp=="B"):
#             score+=1 ##AY
#         else:
#             score+=7 ##AZ
#     elif(me=="Y"):
#         if(opp=="A"):
#             score+=8 ##BX
#         elif(opp=="B"):
#             score+=5 ##BY
#         else:
#             score+=2 ##BZ
#     else:
#         if(opp=="A"):
#             score+=3 ##CX
#         elif(opp=="B"):
#             score+=9 ##CY
#         else:
#             score+=6 ##CZ
# print(score)
    
# inputFile.close()

#PART1

inputFile= open("input.txt", "r")
score=0
for line in inputFile:
    line=line.strip().split(" ")
    end=line[1]
    opp=line[0]
    if(end=="X"):#lose 0 + my choice
        if(opp=="A"):
            score+=3 ##choose scissors
        elif(opp=="B"):
            score+=1 ##choose rock
        else:
            score+=2 ##choose paper
    elif(end=="Y"):#end in a draw 3 + my choice
        if(opp=="A"):
            score+=4 ##choose rock
        elif(opp=="B"):
            score+=5 ##choose paper
        else:
            score+=6 ##choose scissors
    else:#win 6 + my choice
        if(opp=="A"):
            score+=8 ##choose paper
        elif(opp=="B"):
            score+=9 ##choose scissors
        else:
            score+=7 ##choose rock
print(score)
    
inputFile.close()