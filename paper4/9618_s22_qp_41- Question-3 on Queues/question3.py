#a
QueueArray = [None for _ in range(10)]#Array of size 10 type string
HeadPointer = 0 #integer
TailPointer = 0 #integer
NumberItems = 0 #integer

#b
def Enqueue(DataToAdd: str) -> bool:
    global QueueArray, HeadPointer, TailPointer, NumberItems
    if NumberItems == len(QueueArray):
        return False
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else: 
        TailPointer += 1
    NumberItems += 1
    
    return True
    
#c
def Dequeue() -> bool:
    global QueueArray, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return False
    if HeadPointer >= 9:
        HeadPointer = 0
    else:
        HeadPointer += 1
    NumberItems -= 1
    return QueueArray[HeadPointer]
     

#main
#d
for i in range(11):
    x = str(input("Please input a string: "))
    if Enqueue(x):
        print("Enqueue Success")
    else:
        print("Enqueue Failed")

print(Dequeue())
print(Dequeue())

