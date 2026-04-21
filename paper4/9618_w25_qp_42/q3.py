#b
def AddNode(x: int):
    global FreeNode
    global RootPointer
    if FreeNode != -1:
        TreeArray[FreeNode][1] = x
        if RootPointer == -1:
            RootPointer = FreeNode
            FreeNode += 1
        else:
            CurrentNode = RootPointer
            while True:
                if x < TreeArray[CurrentNode][1]:
                    if TreeArray[CurrentNode][0] == -1:
                        TreeArray[CurrentNode][0] = FreeNode
                        FreeNode += 1
                        break
                    else:
                        CurrentNode = TreeArray[CurrentNode][0]
                    
                else:
                    if TreeArray[CurrentNode][2] == -1:
                        TreeArray[CurrentNode][2] = FreeNode
                        FreeNode += 1
                        break
                    else:
                        CurrentNode = TreeArray[CurrentNode][2]
    else:
        print("The tree is full")

#d
def WriteAllToFile():
    try:
        file = open("Tree.txt", 'w')
        for i in range(50):
            line = str(TreeArray[i][0]) + "," + str(TreeArray[i][1]) + "," + str(TreeArray[i][2])
            file.write(line)
            file.write("\n")
        
        file.close()
            
    except IOError:
        print("Error")


#main

#a
TreeArray = [[-1 for _ in range(3)] for _ in range(50)]
#2D Array of 50 rows 3 cols of type integer
RootPointer = -1    #int
FreeNode = 0        #int

#c
try:
    file = open("TreeData.txt", 'r')
    for line in file:
        AddNode(int(line.rstrip('\n')))

    file.close()

except FileNotFoundError:
    print(f"File not found")

#e
WriteAllToFile()

