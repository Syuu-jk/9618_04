#a
class Node:
    def __init__(self, TheData):
        self.TheData = TheData #int
        self.NextNode = None #Node

    def GetData(self):
        return self.TheData
    
    def GetNextNode(self):
        return self.NextNode
    
    def SetNextNode(self, node):
        self.NextNode = node
    
class LinkedList:
    def __init__(self):
        self.HeadNode = None #Node

    def InsertNode(self, data):
        NewNode = Node(data)
        NewNode.SetNextNode(self.HeadNode)
        self.HeadNode = NewNode

    def Traverse(self):
        node = self.HeadNode
        concat = ""
        while node.GetNextNode() != None:
            concat = concat + str(node.GetData()) + " "
            node = node.GetNextNode()       
        return concat + str(node.GetData())
    
    def RemoveNode(self, se):
        node = self.HeadNode
        if node == None:
            return False
        
        if node.GetData() == se:
            self.HeadNode = node.GetNextNode()
        else:
            while node.GetNextNode() != None:
                prev = node
                node = node.GetNextNode()
                if node.GetData() == se:
                    prev.SetNextNode(node.GetNextNode())
                    return True
            return False
        
List = LinkedList()
List.InsertNode(10)
List.InsertNode(20)
List.InsertNode(30)
List.InsertNode(40)
List.InsertNode(50)
print(List.Traverse())
List.RemoveNode(30)
print(List.Traverse())

            
            

    
