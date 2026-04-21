#a
class node:
    def __init__(self, data: int, nextNode: int):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return f"Data: {self.data} | Next Node: {self.nextNode}"
    
    def retData(self):
        return (f"Data: {self.data}")

    def retNextNode(self):
        return self.nextNode

    def setData(self, newData):
        self.Data = newData

    def setNextNode(self, newNextNode):
        self.nextNode = newNextNode
    
#main
#b
global linkedList,startPointer, emptyList
linkedList = [
    node(1,1),
    node(5,4),
    node(6,7),
    node(7,-1),
    node(2,2),
    node(0,6),
    node(0,8),
    node(56,3),
    node(0,9),
    node(0,-1)
]

startPointer: int = 0
emptyList: int = 5

#c
def outputNodes(linkedList = linkedList, startPointer = startPointer):
    
    while startPointer != -1:
            print(linkedList[startPointer].retData())
            startPointer = linkedList[startPointer].retNextNode()
        


#d
def addNode(linkedList = linkedList, startPointer = startPointer, emptyList = emptyList): #passed by reference
    x = int(input("Please input data to be added to the end of the linked list: "))


    
    if emptyList == -1:
        print("There are no empty nodes.")
        return False, startPointer, emptyList
    else:

        TempPointer = emptyList
        emptyList = linkedList[TempPointer].retNextNode()
        linkedList[TempPointer] = node(x, -1)

        i = startPointer
        prev = -1
        while i != -1:
            prev = i
            i = linkedList[i].retNextNode()

        linkedList[prev].setNextNode(5)

       
        

    return True, startPointer, emptyList


#main
outputNodes()
retValue, startPointer, emptyList = addNode()
if retValue:
    print("Success")
else:
    print("Fail")
outputNodes()
