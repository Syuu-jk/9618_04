class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID  #STRING
        self.__MaxSpeed = MaxSpeed  #INTEGER
        self.__CurrentSpeed = 0  #INTEGER
        self.__IncreaseAmount = IncreaseAmount  #INTEGER
        self.__HorizontalPosition = 0 #INTEGER

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, New_Speed): #New_Speed is of type INTEGER
        self.__CurrentSpeed = New_Speed

    def SetHorizontalPosition(self, New_Pos): #New_Pos is of type INTEGER
        self.__HorizontalPosition = New_Pos

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount

        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed

    def GetID(self):
        return self.__ID

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, Vertical_Change, Max_Height):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.__VerticalPosition = 0 #INTEGER
        self.__VerticalChange = Vertical_Change #INTEGER
        self.__MaxHeight = Max_Height   #INTEGER

    def GetVerticalPosition(self):
        return self.__VerticalPosition
    
    def IncreaseSpeed(self):
        super().IncreaseSpeed()
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight


def print_position_speed(vehicle_x):
    #GetID is a getter that returns the ID
    print(f"{vehicle_x.GetID()} Horizontal Position: {vehicle_x.GetHorizontalPosition()}")
    print(f"{vehicle_x.GetID()} Speed: {vehicle_x.GetCurrentSpeed()}")
    
    if isinstance(vehicle_x, Helicopter):
    #if type(vehicle_x) is Helicopter:
    #if vehicle_x.__class__ == Helicopter:

        print (f"{vehicle_x.GetID()} Vertical Position: {vehicle_x.GetVerticalPosition()}")
        #GetVerticalPosition is a getter that returns the vertical position of a helicopter
#main
Car = Vehicle("Tiger", 100, 20)
Heli = Helicopter("Lion", 350, 40, 3, 100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
print_position_speed(Car)
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
print_position_speed(Heli)