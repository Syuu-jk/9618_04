#a
global LinkedList, FirstNode, FirstEmpty
LinkedList = [[-1 for _ in range(2)] for _ in range(20)]
for i in range(19):
    LinkedList[i][1] = i + 1
LinkedList[19][1] = -1
#array of type integer size 20

FirstNode= -1
FirstEmpty = 0

#b
def InsertData(a, b, c, d, e):
    global LinkedList, FirstEmpty, FirstNode
    if FirstEmpty == -1:
        print("Linked list is full")
        pass
    else:
        tup = [a, b, c, d, e]
        for i in range(len(tup)):
            temp = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = tup[i]
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = temp
            


#c
def OutputLinkedList():
    global FirstNode
    temp = FirstNode
    print(FirstNode)
    while FirstNode != -1:
            print(LinkedList[FirstNode][0])
            FirstNode = LinkedList[FirstNode][1]
        
    FirstNode = temp

#d
def RemoveData(data: int):
    global FirstNode
    temp = FirstNode
    while FirstNode != -1:
         if LinkedList[FirstNode][0] == data:
              LinkedList[FirstNode][0] = -1
              LinkedList[prev][1] = LinkedList[FirstNode][1]
              break
         else:
              prev = FirstNode
              FirstNode = LinkedList[FirstNode][1]
         
    FirstNode = temp




#main

InsertData(5, 1, 2, 3, 8)
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()
