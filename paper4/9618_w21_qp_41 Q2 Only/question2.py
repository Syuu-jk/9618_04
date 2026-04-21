class Picture:
    def __init__(self, desc, w, h, fc):
        self.desc = desc    #string
        self.w = w          #integer
        self. h = h         #integer
        self.fc = fc        #string

    def GetDescription(self):
        return self.desc
    
    def GetHeight(self):
        return self.h

    def GetWidth(self):
        return self.w
    
    def GetColour(self):
        return self.fc
    
    def SetDescription(self,newDesc):
        self.desc = newDesc


def readData():
    try:
        file = open("Pictures.txt",'r')
        count = 0   #count is of type integer
    
        while True:
            des = file.readline().strip()
            if des == "":
                file.close()
                return count
            wid = int(file.readline().strip())
            hei = int(file.readline().strip())
            frc = file.readline().strip()
            picA[count] = (Picture(des,wid,hei,frc))
            count += 1

    

    except FileNotFoundError as e:
        print(f"File not Found! {e}")





picA = [None]*100 #of type Picture
readData()

fcol = str(input("Input your desired frame colour: ")).lower()
maxw = int(input("Input the maximum width: "))
maxh = int(input("Input the maximum height: "))

for i in range(len(picA)): 
    if picA[i] != None:
        if (picA[i]).GetColour() == fcol:
            if (picA[i]).GetWidth() <= maxw and (picA[i]).GetHeight() <= maxh:
                print (f"Description: {picA[i].GetDescription()}\nWidth: {picA[i].GetWidth()}\nHeight: {picA[i].GetHeight()}\nFrame Colour: {picA[i].GetColour()}\n")

