#a
DataArray = [None for _ in range(100)]#OF TYPE INTEGER SIZE 100

#b
def ReadFile():
    try:
        file = open("paper4\\9618_w22_qp_41 Question Number-1\\IntegerData.txt", 'r')
        for i in range(100):
            DataArray[i] = int(file.readline().strip())

        file.close()

    except FileNotFoundError as e:
        print(f"File Not Found! {e}")

#c
def FindValues():
    count = 0
    x = int(input("Please input a whole number between 1 and 100 inclusive: "))
    for i in range(100):
        if x == DataArray[i]:
            count += 1
    return count

#d

print("\nLinear Search + Bubble Sort\n")

ReadFile()
print(f"Number appears {FindValues()} times in the array")

#e
def BubbleSort():
    x = len(DataArray)-1
    Swap = True
    temp = None

    while Swap and x > 0:
        Swap = False
        for j in range(x):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp
                Swap = True
        x -= 1
    
    print(DataArray)

BubbleSort()

print("\nInsertion Sort + Binary Sort\n")

#Insertion Sort Binary Sort
def InsertionSort():
    for i in range(1, len(DataArray)):
        Key = DataArray[i]
        j = i - 1
        while j > -1 and DataArray[j] > Key:
            DataArray[j + 1] = DataArray[j]
            j -= 1
        DataArray[j + 1] = Key

    print(DataArray)

def BinarySearch():
    x = int(input("Please input a whole number between 1 and 100 inclusive: "))
    Found = False
    Low = 0
    High = len(DataArray) - 1
    while Low <= High and not Found:
        Mid = (Low + High) // 2
        if DataArray[Mid] == x:
            Found = True
            break
        elif DataArray[Mid] < x:
            Low = Mid + 1
        else:
            High = Mid - 1

    if Found:
        index = Mid
        more = True
        less = True
        count = 1
        
        while more:
            more = False
            if Mid + 1 < len(DataArray) and DataArray[Mid + 1] == x:
                Mid += 1
                more = True
                count += 1

        Mid = index

        while less:
            less = False
            if Mid - 1 > -1 and DataArray[Mid - 1] ==  x:
                Mid -= 1
                less = True
                count += 1
    
        return count
    
InsertionSort()
print(f"Number appears {BinarySearch()} times in the array")
