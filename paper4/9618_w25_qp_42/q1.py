class Bird:
    def __init__(self, DistancePerHour: float, Species: str):
        self.DistancePerHour = DistancePerHour
        self.Species = Species      #STRING
        self.XPosition = 500.0  #REAL
        self.YPosition = 500.0  #REAL

    def GetSpecies(self):
        return self.Species
    
    def GetPosition(self):
        return f"X = {self.XPosition} Y = {self.YPosition}"

    def Move(self, dir: str, time: int):
        DistanceTravelled = (self.DistancePerHour/60)*time
        match dir:
            case 'N':
                 self.YPosition += DistanceTravelled
            case 'S': 
                self.YPosition -= DistanceTravelled 
            case 'E':
                self.XPosition += DistanceTravelled
            case 'W':
                self.YPosition -= DistanceTravelled

    
#main
Bird1 = Bird(71.0, "Cockatiel")
Bird2 = Bird(56.0, "Macaw")
                
Bird1.GetSpecies()
Bird1.GetPosition()
Bird2.GetSpecies()
Bird2.GetPosition()
while True: 
    chosen = int(input("Please select a bird to move: "))
    if chosen == 1 or chosen == 2:
        break
while True:
    dir = str(input("Please enter the direction of travel: "))
    match dir:
        case 'W' | 'E' | 'N' | 'S': break
while True:       
    time = int(input("Please enter the time of travel to the nearest minute: "))
    if time <= 500 and time >= 0:
        break 
if chosen == 1:
    Bird1.Move(dir, time)
    print(Bird1.GetPosition())
else:
    Bird2. Move(dir, time)
    print(Bird2.GetPosition())