ArrayNodes = [[None for _ in range(3)] for _ in range(20)] #2d array of type integer 3 col 20 row
RootPointer = -1 #int
FreeNode = 0 #int

def AddNode(ArrayNodes: list, RootPointer: int, FreeNode: int):
    print("Enter the data")
    NodeData = int(input(""))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")

    return FreeNode, RootPointer

def PrintAll():
    for i in range(FreeNode):
        LP = ArrayNodes[i][0]
        DT = ArrayNodes[i][1]
        RP = ArrayNodes[i][2]
        print(f"{LP}    {DT}    {RP}")


def InOrder(currentNode):
    global ArrayNodes
    if currentNode != -1:
        InOrder(ArrayNodes[currentNode][0])
        print(ArrayNodes[currentNode][1])
        InOrder(ArrayNodes[currentNode][2])
    



#main
for i in range(10):
    FreeNode, RootPointer = AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll()

InOrder(RootPointer)