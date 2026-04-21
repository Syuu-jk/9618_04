class Card:
    def __init__(self, number, colour):
        self.__number = number # OF TYPE INTEGER
        self.__colour = colour # OF TYPE STRING


    def GetNumber(self):
        return self.__number
    
    def GetColour(self):
        return self.__colour


def ChooseCard():
    global selected_card_index
    card_index = 999 # OF TYPE INTEGER

    while True:
        card_index = (int(input("Please input a number between 1 and 30 inclusive: "))) - 1
        if card_index > 29 or card_index < 0:
            print("Number must be between 1 and 30 inclusive")
        elif card_index in selected_card_index:
            print("Already Taken")
        else: 
            break

    selected_card_index.append(card_index)
    return card_index
    
#Main

selected_card_index = [] #OF TYPE INTEGER
CardArr = [None for _ in range(30)] #OF TYPE Card

try:
    file = open("CardValues.txt",'r')
    i = 0 
    while True:
        num = (file.readline().strip()) 
        if num == "":
            break
        col = file.readline().strip() 
        CardArr[i] = Card(int(num), col)
        i += 1
          
        
except FileNotFoundError as e:
    print(f"File Not Found {e}")

else:
    file.close()



Player1 = [None for _ in range(4)]
for i in range(4):
    Player1[i] = CardArr[ChooseCard()]
for i in range(4):
    print(f"Card Number: {Player1[i].GetNumber()}\nCard Colour: {Player1[i].GetColour()} ")