class Character:
    def __init__(self, name, x, y):
        self.__name = name  #OF TYPE STRING
        self.__x = x    #OF TYPE INTEGER
        self.__y = y    #OF TYPE INTEGER
    
    def GetName(self):
        return self.__name
    
    def GetX(self):
        return self.__x
    
    def GetY(self):
        return self.__y
    
    def ChangePosition(self,delta_x, delta_y):
        self.__x += delta_x 
        self.__y += delta_y 

    def __str__(self):
        return f"Name: {self.__name}\nX: {self.__x}\n Y: {self.__y}"

    
#main
character_array = [None for _ in range (10)] #OF TYPE Character

try:
    file = open("paper4/9618_w22_qp_42 OOP Q2 ONLY/Characters.txt", 'r')
    i = 0   #OF TYPE INTEGER
    while True:
        name = file.readline().strip()
        if name == "": break
        x = int(file.readline().strip())
        y = int(file.readline().strip())
        character_array[i] = Character(name, x, y)
        i += 1

except FileNotFoundError as e:
    print(f"File not found {e}")

else:
    file.close()

index_pos = -1 #OF TYPE INTEGER
attempts = 1 #OF TYPE INTEGER
while True: 
    if attempts > 1:
        print("Character Not Found!")
    ask_name = str(input("Please input a character name: ")).capitalize().strip()
    attempts += 1
    
    # for i in range(10):
    #     if character_array[i].GetName() == ask_name:
    #         index_pos = i
    #         break
    # attempts += 1 

    if any(char.GetName() == ask_name for char in character_array) == True:
        index_pos = next(i for i, char in enumerate(character_array) if char.GetName() == ask_name)
        print(index_pos)
        break
        
    

move_key = str(input("(W/A/S/D) Please input a movement key: ")). upper()
while move_key != "W" and move_key != "A" and move_key != "S" and move_key != "D":
    move_key = str(input("(W/A/S/D) Please input a valid movement key: ")). upper()

match move_key:
    case "W":
        character_array[index_pos].ChangePosition(0,1)
    case "A":
        character_array[index_pos].ChangePosition(-1,0)
    case "S":
        character_array[index_pos].ChangePosition(0,-1)
    case "D":
        character_array[index_pos].ChangePosition(1,0)    


print(f"{character_array[index_pos].GetName()} has changed coordinates to X = {character_array[index_pos].GetX()} and Y = {character_array[index_pos].GetY()}")
