#a
class Node:
    def __init__(self, LeftPointer: int = -1, Data: int = 0, RightPointer: int = -1):

        self.LeftPointer = -1
        self.Data = 0
        self.RightPointer = -1

    def GetLeft(self):
        return self.LeftPointer    
    
    def GetData(self):
        return self.Data
    
    def GetRight(self):
        return self.RightPointer
    
    def SetLeft(self, LeftPointer):
        self.LeftPointer = LeftPointer

    def SetData(self, Data):
        self.Data = Data

    def SetRight(self, RightPointer):
        self.RightPointer = RightPointer

#b
class TreeClass:
    
    def __init__(self, Tree: list = [Node(0,0,0) for _ in range(20)], FirstNode: int = -1, NumberNodes: int = 0):
        self.Tree = [Node(0,0,0) for _ in range(20)]
        self.FirstNode = -1
        self.NumberNodes = 0

    def InsertNode(self, NewNode: Node):

        self.Tree[self.NumberNodes] = NewNode

        if self.FirstNode == -1:
            self.NumberNodes += 1
            self.FirstNode = 0

        else:
            CurrentNode = self.FirstNode
            while True:
                if NewNode.GetData() < self.Tree[CurrentNode].GetData():
                    if self.Tree[CurrentNode].GetLeft() == -1:
                        self.Tree[CurrentNode].SetLeft(self.NumberNodes)
                        self.NumberNodes += 1
                        break
                    else:
                        CurrentNode = self.Tree[CurrentNode].GetLeft()
                else:
                    if self.Tree[CurrentNode].GetRight() == -1:
                        self.Tree[CurrentNode].SetRight(self.NumberNodes)
                        self.NumberNodes += 1
                        break
                    else:
                        CurrentNode = self.Tree[CurrentNode].GetRight()
        
    def OutputTrees(self):
        if self.NumberNodes > 0:
            for i in range(self.NumberNodes):
                print(f"{self.Tree[i].GetLeft()} | {self.Tree[i].GetData()} | {self.Tree[i].GetRight()}")
        else:
            print("No nodes")

#main
#c
TheTree = TreeClass()
for _ in range(7):
    x = int(input("Enter data: "))
    NewNode = Node()
    NewNode.SetData(x)
    TheTree.InsertNode(NewNode)
TheTree.OutputTrees()