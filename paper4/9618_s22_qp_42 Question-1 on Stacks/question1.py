#a
global StackData, StackPointer
StackData = [None for _ in range(10)] #array of size 10 type integer
StackPointer = 0 #type integer

#b
def print_stack():
    for i in range(10):
        print(f"Data_Index {i}: {StackData[i]}")
    print(f"Stack Pointer: {StackPointer}")


#c
def Push(x: int) -> bool:
    global StackData, StackPointer
    if StackPointer > len(StackData) - 1:
        return False
    else:
        StackData[StackPointer] = x
        return True

#e
def Pop() -> int:
    global StackData, StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer -= 1
        return StackData[StackPointer]

#main

#d
for i in range(11):
    x = int(input("Enter an integer to push onto the stack: "))
    if Push(x):
        StackPointer += 1
        print("Push Success")
    else:
        print("Stack Overflow")

print_stack()
#e
Pop()
Pop()
print_stack()