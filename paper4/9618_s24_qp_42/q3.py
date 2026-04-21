#b
def RecursiveInsertion(IntegerArray: list, NumberElements: int) -> list:
    if NumberElements <= 1:
        return IntegerArray
    
    else:

        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2

    LoopAgain = True

    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False

    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

#c
def IterativeInsertion(IntegerArray: list, NumberElements: int) -> list:
    if NumberElements <= 1:
        return IntegerArray
    
    for i in range(1, NumberElements):

        LastItem = IntegerArray[i]
        CheckItem = i - 1
        LoopAgain = True

        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False

        while LoopAgain:

            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem -= 1
            if CheckItem < 0:
                LoopAgain = False
            else:
                if IntegerArray[CheckItem] < LastItem:
                    LoopAgain = False

        IntegerArray[CheckItem + 1] = LastItem

    return IntegerArray

#d
def BinarySearch(IntegerArray: list, First: int, Last: int, ToFind: int) -> int:
    Mid = (First + Last) //2
    if First > Last:
        return -1
    if IntegerArray[Mid] == ToFind:
        return Mid
    if IntegerArray[Mid] < ToFind:
        return BinarySearch(IntegerArray, Mid + 1, Last, ToFind)
    return BinarySearch(IntegerArray, First, Mid - 1, ToFind)
    


#main
#a
NumberArray = [100, 85, 644, 22 , 15 , 8, 1]
print("Recursive")
print(RecursiveInsertion(NumberArray, len(NumberArray) ))
print("iterative")
print(IterativeInsertion(NumberArray, len(NumberArray) ))
i = BinarySearch(NumberArray, 0, len(NumberArray) - 1, 644)
if i != -1:
    print(f"Found at index {i}")
else:
    print("Not found")