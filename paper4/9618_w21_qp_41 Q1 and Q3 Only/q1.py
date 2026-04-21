def Unknown(X:int, Y:int) -> int:
    if X < Y: 
        print(X + Y)
        return(Unknown(X+1, Y)* 2)
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return (Unknown(X-1, Y) // 2)
        


def IterativeUnknown(X: int, Y: int) -> int:
        if X < Y:    
            for i in range(X+Y, 2*Y):
                print(i)
        elif X == Y:
            pass
        else:
             for i in range(X+Y, 2*Y, -1):
                  print(i)

        return int(2**(Y-X)//1)



#main


print("X: 10, Y: 15")
print(Unknown(10,15))
print("X: 10. Y: 10")
print(Unknown(10,10))
print("X: 15, Y: 10")
print(Unknown(15,10))


print("X: 10, Y: 15")
print(IterativeUnknown(10,15))
print("X: 10. Y: 10")
print(IterativeUnknown(10,10))
print("X: 15, Y: 10")
print(IterativeUnknown(15,10))
        

