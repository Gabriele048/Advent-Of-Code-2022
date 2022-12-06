#PART1
inputFile= open("input.txt", "r")

def isMarker(packet):
    p=[]
    for c in packet:
        p.append(c)
    for char in p:
        if p.count(char)>1:
            return False
    return True

for line in inputFile:
    stream=line.strip()
for i in range(len(stream)):
    ##PART1: UNCOMMENT THIS SECTION
    # if isMarker(stream[i:i+4]):
    #     print(i+4)
    #     break

    #PART2: UNCOMMENT THIS SECTION
    if isMarker(stream[i:i+14]):
        print(i+14)
        break

inputFile.close()