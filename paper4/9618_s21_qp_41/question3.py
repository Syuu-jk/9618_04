class TreasureChest:
    def __init__(self,question,answer,points):
        self.__question = question  # TYPE STRING
        self.__answer = answer      # TYPE INTEGER
        self.__points = points      # TYPE INTEGER



    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self,ans): #ans is of type integer
        if ans == self.__answer:
            return True
        else:
            return False

    def getPoints(self,na): #na is of type integer
         if na == 1:
             return self.__points
         elif na == 2:
             return self.__points//2
         elif na > 4:
             return 0
         else:
             return self.__points//4

def readData():
    try:
        file = open("TreasureChestData.txt",'r')
        global arrayTreasure
        arrayTreasure = [TreasureChest(None, None, None)] # OF TYPE TreasureChest
        #DECLARE quest: STRING
        #DECLARE ansa: INTEGER
        #DECLARE pts: INTEGER
        line = file.readline() #line is of type STRING
        while line != "":
            quest = line.strip()
            ansa = int(file.readline().strip())
            pts = int(file.readline().strip())
            line = file.readline()
            arrayTreasure.append(TreasureChest(quest,ansa,pts))

    except FileNotFoundError as e: 
        print(f"File Not Found! {e}")

    else:
        file.close()


    

readData()
qsno = int(input("Input a question number 1 to 5: "))
if 1 <= qsno <= 5:
    chest = arrayTreasure[qsno-1]
    print(chest.getQuestion())

    correct = False
    noAttempts = 1

    while correct == False:
        userAns = int(input("Input your answer: "))
        if chest.checkAnswer(userAns):
            print("Correct Answer!")
            break
        else:
            noAttempts += 1
            print("Try Again!")
            
    pointsEarned = chest.getPoints(noAttempts)
    print(f"Points Earned: {pointsEarned}")
