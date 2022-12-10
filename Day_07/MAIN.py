#PART1
inputFile= open("input.txt", "r")

class File:
    def __init__(self, size, name):
        self.name = name
        self.size = size
    def getSize(self):
        return self.size
    def getName(self):
        return self.name

class Directory:
    def __init__(self, parentDirectory, name):
        self.parentDirectory = parentDirectory
        self.name = name
        self.childDirectories = []
        self.childFiles = []
    def getSize(self):
        size = 0
        for d in self.childDirectories:
            size += d.getSize()
        for f in self.childFiles:
            size += f.getSize()
        return size
    def getName(self):
        return self.name
    def addDirectory(self, dir):
        self.childDirectories.append(dir)
    def addFile(self, file):
        self.childFiles.append(file)
    def getAllDir(self):
        return self.childDirectories
    def getFiles(self):
        return self.childFiles
    def getParent(self):
        return self.parentDirectory
    def getChild(self, name):
        for dir in self.childDirectories:
            if name == dir.getName():
                return dir
allDirectories=[]
rootDirectory = Directory(None, "/")
currentDirectory = Directory(None, "/")

for line in inputFile:
    line=line.strip().split(" ")
    if(line[0] == "$"):
        #COMMAND
        if(line[1] == "cd"):
            if(line[2] == "/"):
                currentDirectory = rootDirectory
            elif (line[2] == ".."):
                currentDirectory = currentDirectory.getParent()
            else:
                currentDirectory = currentDirectory.getChild(line[2])
        
    elif(line[0] == "dir"):
        #DIRECTORY
        newDir  = Directory(currentDirectory, line[1])
        currentDirectory.addDirectory(newDir)
        allDirectories.append(newDir)

    else:
        #FILE
        #print(type(int(line[0])), "\t", line[1])
        f = File(int(line[0]), line[1])
        currentDirectory.addFile(f)
count=0
for directory in allDirectories:
    if directory.getSize() < 100000:
        count += directory.getSize()
totalUsedSpace = rootDirectory.getSize()
print("PART1: ", count)
print("TotalUsed: ", totalUsedSpace)


totalSpace = 70000000
unusuedSpaceRequired = 30000000
candidateSize = [] 
for d in allDirectories:
    if(totalSpace - totalUsedSpace + d.getSize()) > unusuedSpaceRequired:
        candidateSize.append(d.getSize())
print("PART2: ", min(candidateSize))


inputFile.close()