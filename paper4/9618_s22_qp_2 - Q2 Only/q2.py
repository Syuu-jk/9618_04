#ii
def printArr():
    for i in range(10):
        row = ""
        for j in range(10):
            num = str(ArrayData[i][j])
            if len(num) == 1:
                num = num + " "
            row = row + num + " "
        
        print(row.strip())

#c
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:  
        Mid = (Lower + (Upper -1))//2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
        
    return -1


#main
import random

#a
ArrayData = [[ 0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        ArrayData[i][j] = random.randint(1,100)

printArr()
#b
ArrayLength = 10
for X in range(0, ArrayLength ):
    for Y in range(0, ArrayLength - 1):
        for Z in range(0, ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z+1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue
print()

printArr()

print(BinarySearch(ArrayData, 0, len(ArrayData), 14))

print(BinarySearch(ArrayData, 0, len(ArrayData), 18))