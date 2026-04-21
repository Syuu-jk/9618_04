#a
def ReadTouristData():
    DataArray = [[None for _ in range(5)]for _ in range(10)] #Array of TYPE STRING 10 rows, 5 columns
    filename = str(input("Please enter a file name: ")) #string

    try: 
        file = open(filename, 'r')
        i = 0 #integer
        for line in file: #line is string
            splitedLine = line.strip().split(',')
            for j in range(5):
                DataArray[i][j] = splitedLine[j]
            i += 1
        
        file.close()
        return DataArray
    
    

    except FileNotFoundError:
        print(f"File not found")
    
#b
def TotalVisitors(DataArr, CityName): #DataArr is array of type STRING, CityName is string
    Found = False #boolean
    for i in range(len(DataArr)):
        if DataArr[i][0] == CityName:
            Found = True
            break
    if Found:
        Total = 0 #integer
        for j in range(1, 5):
            Total += int(DataArr[i][j])
        print(f"Total number of tourists who visited {CityName} in the year : {Total}") 
    else:
        print("City Not Found")

#c
def MostVisitorsInQuarter(DataArr, Qn): #DataArr is array of type STRING, Qn is INTEGER
    Max = 0 #integer
    index = -1 #integer
    otherHighest = [] #1d array of type string

    for i in range(len(DataArr)):

        if int(DataArr[i][Qn]) > Max:
            Max = int(DataArr[i][Qn])
            index = i 
            otherHighest = []

        elif int(DataArr[i][Qn]) == Max:
                otherHighest.append((DataArr[i][Qn]))
                otherHighest.append(DataArr[i][0])

    print(f"{DataArr[index][0]} has {Max} visitors in Quarter {Qn}")

    for j in range(0, len(otherHighest), 2):
        print(f"{otherHighest[j+1]} has {otherHighest[j]} visitors in Quarter {Qn}")
    

#d
def ExportQuarterFiles(DataArr):
    for i in range(1,5):
        try:
            filename = "Quarter" + str(i) + ".txt"
            file = open(filename, 'w')
            for j in range(10):
                file.write(f"{DataArr[j][0]},{DataArr[j][i]}\n") 
            
            file.close()
        
        except FileNotFoundError:
            print("File not found")


#e
#main
DataArray = ReadTouristData()
TotalVisitors(DataArray, "Paris")
MostVisitorsInQuarter(DataArray, 4)
ExportQuarterFiles(DataArray)