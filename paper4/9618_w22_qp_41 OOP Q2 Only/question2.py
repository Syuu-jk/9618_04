class Card:
    def __init__(self, number , colour):
        self.__number = number #OF TYPE INTEGER
        self.__colour = colour #OF TYPE STRING

    def GetNumber(self):
        return self.__number
    
    def GetColour(self):
        return self.__colour
    
    def __str__(self):
        return(self.__number, self.__colour)
    
class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        self.__cards = [c1, c2, c3, c4, c5] #ARRAY OF TYPE Card
        for i in range(5):
            self.__cards.append(None)
        self.__FirstCard = 0    #OF TYPE INTEGER
        self.__NumberCards = 5  #OF TYPE INTEGER
        

    def GetHand(self, index):
        return self.__cards[index] #index is OF TYPE INTEGER

def CalculateValue(player_hand):
    score = 0
    for i in range(5):
        this_card = player_hand.GetHand(i)
        if this_card.GetColour() == "red":
            score += 5
        elif this_card.GetColour() == "blue":
            score += 10
        elif this_card.GetColour() == "yellow":
            score += 15
    return score



#Main
cards_all = []
colours_array = ["red", "blue", "yellow"]

for i in range(1,6):
    for colour in colours_array:
        cards_all.append(Card(i,colour))

r1 = Card(1, "red")
r2 = Card(2, "red")
r3 = Card(3, "red")
r4 = Card(4, "red")
r5 = Card(5, "red")
b1 = Card(1, "blue")
b2 = Card(2, "blue")
b3 = Card(3, "blue")
b4 = Card(4, "blue")
b5 = Card(5, "blue")
y1 = Card(1, "yellow")
y2 = Card(2, "yellow")
y3 = Card(3, "yellow")
y4 = Card(4, "yellow")
y5 = Card(5, "yellow")

Player1 = Hand(r1, r2, r3, r4, y1)
Player2 = Hand(y2, y3, y4, y5, b1)

score_1 = CalculateValue(Player1)
score_2 = CalculateValue(Player2)
diff = score_1 - score_2
if diff == 0:
    print("The game is a draw")
elif diff > 0:
    print("Player 1 has won the game")
elif diff < 0:
    print("Player 2 has won the game")