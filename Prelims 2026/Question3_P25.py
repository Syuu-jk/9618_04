#a
class Node():
    def __init__ (self, NodeData):
        self.NodeData = NodeData    #STRING
        self.LeftNode = None    #Node
        self.RightNode = None  #Node
        #None is for Null Node

    def GetLeft(self):
        return self.LeftNode

    def GetRight(self):
        return self.RightNode

    def GetData(self):
        return self.NodeData
    
    def SetLeft(self, newLeft): 
        self.LeftNode = newLeft     #Node

    def SetRight(self, newRight): 
        self.RightNode = newRight   #Node

#c
class Tree:
    def __init__(self, FirstNode):
        self.FirstNode = FirstNode #Node

    def GetRootNode(self):
        return self.FirstNode

    def Insert(self, NewNode):
        #None is null node
        currentNode = self.FirstNode#node
        
        while True:

            if NewNode.GetData() < currentNode.GetData():

                if currentNode.GetLeft() == None:
                    currentNode.SetLeft(NewNode)
                    break
                else:
                    currentNode = currentNode.GetLeft()

            else:

                if currentNode.GetRight() == None:
                    currentNode.SetRight(NewNode) 
                    break
                else:
                    currentNode = currentNode.GetRight()


#d
def OutputInOrder(thisNode):
    #None is null node
    if thisNode.GetLeft() != None: 
        OutputInOrder(thisNode.GetLeft())
    if thisNode.GetLeft() == None:
        print(thisNode.GetData().strip())
    if thisNode.GetRight() != None:
        OutputInOrder(thisNode.GetRight())


#main
#b
NodeArr = [] #array of type Node
try:
    file = open("StudentNames.txt", 'r') 
    for line in file: #line is tring
        NodeArr.append(Node(line, None, None)) #None is a null node
    
    file.close()

except FileNotFoundError:
    print("File not found")

#e
NameBinTree = Tree(NodeArr[0]) 
for i in range(1, len(NodeArr)):
    NameBinTree.Insert(NodeArr[i])



OutputInOrder(NameBinTree.GetRootNode())