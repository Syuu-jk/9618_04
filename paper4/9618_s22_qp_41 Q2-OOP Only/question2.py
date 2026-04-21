class Balloon:
    def __init__(self, Colour, DefItem, Health = 100):
        self.__Health = Health  #OF TYPE INTEGER
        self.__Colour = Colour  #OF TYPE STRING
        self.__DefItem = DefItem#OF TYPE STRING

    def GetDefenceItem(self):
        return self.__DefItem
    
    def ChangeHealth(self, delta_health): #delt_health is of type integer
        self.__Health += delta_health
    
    def CheckHealth(self):
        if self.__Health > 0:
            return False
        else:
            return True
    
    def __str__(self):
        return(f"Health: {self.__health}\nColour: {self.__Colour}\nDefence Item: {self.__DefItem}")


def Defend(Bal): #Bal is an object of type Balloon
    strength = int(input("Please input strength of opponent: "))
    Bal.ChangeHealth(-strength)
    print(Bal.GetDefenceItem(), "has been used")
    if Bal.CheckHealth() == True:
        print("Balloon has no health remaining")
    else:
        print("Balloon still has health remaining")
    return(Bal)


user_def_item = str(input("Please input a defence item: "))
user_colour = str(input("Please input a colour: "))
Balloon1 = Balloon(user_colour, user_def_item)
Defend(Balloon1)

