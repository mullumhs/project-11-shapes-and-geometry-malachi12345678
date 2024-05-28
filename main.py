from shapes import Shape , Rect , Circle

while True:
    print("SHAPE CALCULATOR")
    userChoice = input("press R for rectangle or C for circle       ")
        
    if userChoice.upper() == "R":
        print("rectangle selected")
        W = input("enter width")
        H = input("enter height")

        
        
        userRect = Rect( W , H)
        
        print("perimeter = " , userRect.perimeter())
        print("area = " , userRect.area())

    elif userChoice.upper() == "C":
        print("circle selected")
        R = input("enter radius")
        
        userCircle = Circle(R)
        print(userCircle.perimeter())
        print(userCircle.area())

    else:
        print("invalid input")
        continue
        


