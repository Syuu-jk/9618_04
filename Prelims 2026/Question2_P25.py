#a
class Stack:
    def __init__(self, StackArray, TopPointer):
        self.StackArray = StackArray #array of type integer size 100
        self.TopPointer = TopPointer    #integer

    def getTop(self):
        return self.TopPointer

    def getStackArr(self):
        return self.StackArray

    def setTop(self, newTop):
        self.TopPointer = newTop
    
#c
def Push(x): #x is integer
    if TheStack.getTop() < 99:
        TheStack.setTop(TheStack.getTop() + 1)
        TheStack.getStackArr()[TheStack.getTop()] = x
    else:
        return -1

#d
def ReturnAllData():
    concatval = "" #string
    for i in range(TheStack.getTop(), -1, -1):
        concatval = concatval + str(TheStack.getStackArr()[i]) + " "

    return (concatval.strip())

#f
def Pop():
    top = TheStack.getTop() #int
    if top == -1:
        return -1
    TheStack.setTop(top -1)
    return TheStack.getStackArr()[top] 


#main

#b
stackArr = [-1 for _ in range(100)] #1d array of size 100 type integer
TheStack = Stack(stackArr, -1)

#e
try:
    file = open("Numbers.txt", 'r')
    count = 0 #integer
    for line in file:
        if int(line.strip()) >= 0:
            if Push(int(line.strip())) == -1:
                print("stack is full")
            else:
                count += 1
                print("succesfully added")
        if count == 10: break
    print(ReturnAllData())

    file.close()

except FileNotFoundError:
    print("File not found")

#g
for _ in range(2):
    val = Pop() #int
    if ValueError == -1:
        print("stack is empty")
        break
    else:
        print(val)

print(ReturnAllData())