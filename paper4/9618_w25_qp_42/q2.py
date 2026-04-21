#b
def PrintArray(intarr: int): #intarr is an array of type integer
    line = "" #string
    for i in range(20):
        line +=  str(intarr[i]) + " "
    print(line)

#c
def BubbleSort(intarr: int) -> int: 
    #intarr is an array of type integer 
    #returns an array of type integer
    #top, bot integer
    top = len(intarr) - 1
    bot = 0
    for _ in range(len(intarr)-1):
        for j in range(bot, top):
            if intarr[j] > intarr[j+1]:
                intarr[j] , intarr[j+1] = intarr[j+1], intarr[j]
        top -= 1

    return intarr

#e
def RecursiveBinarySearch(intarr: int, lb : int, ub: int, val: int):
    mid = (lb + ub) //2 #int
    found = False #boolean
    if lb > ub:
        return -1
    if val == intarr[mid]:
        return mid
    elif val > intarr[mid]:
        return RecursiveBinarySearch(intarr, mid+1, ub, val)
    else:
        return RecursiveBinarySearch(intarr, lb, mid-1, val)

    

    
#main
#a
import random

randomarr = [None for _ in range(20)]
for i in range(20):
    while True:
        x = random.randint(0, 100)
        if x not in randomarr:
            randomarr[i] = x
            break



PrintArray(randomarr)
print("Sorted")
print(BubbleSort(randomarr))

se = int(input("Please enter an integer: "))
i = RecursiveBinarySearch(randomarr, 0, 19, se)
if i == -1:
    print("Not found")
else:
    print(f"Found at position {i+1}")