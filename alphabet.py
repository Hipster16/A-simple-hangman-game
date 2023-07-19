import turtle

def letters (l, x=0, y=0 ,col="black") :
    turt=turtle.Turtle()
    turt.color(col)
    turt.penup()
    turt.hideturtle()
    turt.setposition(x, y)
    turt.pensize(7)
    turt.pendown()
    turt.speed("fast")

    if(l=="A"):
        turt.penup()
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.pendown()
        turt.left(70)
        turt.fd(50)
        turt.right(2*70)
        turt.fd(50)
        turt.bk(20)
        turt.right(110)
        turt.fd(20)
        
    
    elif (l=="B"):
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.circle(12.5,180)
        turt.left(180)
        turt.circle(12.5,180)
    
    elif (l=="C"):
        turt.penup()
        turt.fd(25)
        turt.pendown()
        turt.left(180)
        turt.circle(25, 180)
    
    elif(l=="D"):
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.circle(25, 180)
    
    elif(l=="E"):
        turt.fd(30)
        turt.bk(30)
        turt.right(90)
        turt.fd(25)
        turt.left(90)
        turt.fd(20)
        turt.bk(20)
        turt.right(90)
        turt.fd(25)
        turt.left(90)
        turt.fd(30)
    
    elif(l=="F"):
        turt.fd(30)
        turt.bk(30)
        turt.right(90)
        turt.fd(25)
        turt.left(90)
        turt.fd(20)
        turt.bk(20)
        turt.right(90)
        turt.fd(25)
    
    elif(l=="G"):
        turt.penup()
        turt.fd(30)
        turt.pendown()
        turt.left(180)
        turt.circle(25, 180)
        turt.left(90)
        turt.fd(25)
        turt.left(90)
        turt.fd(10)

    elif (l=="H"):
        turt.right(90)
        turt.fd(50)
        turt.bk(25)
        turt.left(90)
        turt.fd(25)
        turt.left(90)
        turt.fd(25)
        turt.bk(50)
    
    elif (l=="I"):
        turt.penup()
        turt.fd(20)
        turt.pendown()
        turt.fd(20)
        turt.bk(40)
        turt.fd(20)
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.fd(20)
        turt.bk(40)

    elif(l=="J"):
        turt.fd(20)
        turt.bk(40)
        turt.fd(20)
        turt.right(90)
        turt.fd(30)
        turt.circle(20, 90)
    
    elif(l=="K"):
        turt.right(90)
        turt.fd(50)
        turt.bk(25)
        turt.left(45)
        turt.fd(30)
        turt.bk(30)
        turt.left(2*45)
        turt.fd(30)
    
    elif(l=="L"):
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.fd(30)
    
    elif(l=="M"):
        turt.right(90)
        turt.fd(50)
        turt.bk(50)
        turt.left(45)
        turt.fd(30)
        turt.left(90)
        turt.fd(30)
        turt.right(135)
        turt.fd(50)
    
    elif(l=="N"):
        turt.right(90)
        turt.fd(50)
        turt.bk(50)
        turt.left(45)
        turt.fd(70)
        turt.left(135)
        turt.fd(50)

    elif(l=="O"):
        turt.penup()
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.fd(20)
        turt.pendown()
        turt.circle(25)

    elif(l=="P"):
        turt.right(90)
        turt.fd(50)
        turt.bk(20)
        turt.left(90)
        turt.circle(15,180)
    
    elif(l=="Q"):
        turt.penup()
        turt.fd(20)
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.pendown()
        turt.circle(25)
        turt.penup()
        turt.fd(20)
        turt.pendown()
        turt.right(45)
        turt.fd(10)
        turt.bk(30)
    
    elif(l=="R"):
        turt.right(90)
        turt.fd(50)
        turt.bk(20)
        turt.left(90)
        turt.circle(15,180)
        turt.left(90)
        turt.fd(20)
        turt.left(45)
        turt.fd(45)
    
    elif(l=="S"):
        turt.penup()
        turt.fd(20)
        turt.right(90)
        turt.fd(50)
        turt.left(90)
        turt.pendown()
        turt.circle(12.5, -40)
        turt.circle(12.5, 40)
        turt.circle(12.5, 180)
        turt.left(190)
        turt.circle(12.5, -220)

    elif(l=="T"):
        turt.penup()
        turt.fd(20)
        turt.pendown()
        turt.fd(20)
        turt.bk(40)
        turt.fd(20)
        turt.right(90)
        turt.fd(50)
    
    elif(l=="U"):
        turt.right(90)
        turt.fd(40)
        turt.circle(15,180)
        turt.fd(40)
    
    elif(l=="V"):
        turt.right(70)
        turt.fd(60)
        turt.left(140)
        turt.fd(65)
    
    elif(l=="W"):
        turt.right(90)
        turt.penup()
        turt.fd(50)
        turt.pendown()
        turt.right(180)
        turt.fd(50)
        turt.bk(50)
        turt.right(45)
        turt.fd(30)
        turt.right(90)
        turt.fd(30)
        turt.left(135)
        turt.fd(50)
    
    elif(l=="X"):
        turt.right(45)
        turt.fd(70)
        turt.bk(35)
        turt.right(90)
        turt.fd(35)
        turt.bk(70)
    
    elif(l=="Y"):
        turt.right(45)
        turt.fd(35)
        turt.right(45)
        turt.fd(35)
        turt.bk(35)
        turt.left(135)
        turt.fd(35)
    
    elif(l=="Z"):
        turt.fd(35)
        turt.right(135)
        turt.fd(60)
        turt.left(135)
        turt.fd(35)
    
    elif(l=="tick"):
        turt.color("green")
        turt.penup()
        turt.right(90)
        turt.fd(60)
        turt.left(90)
        turt.fd(20)
        turt.pendown()
        turt.circle(30)
    
    elif(l=="cross"):
        turt.color("red")
        turt.right(45)
        turt.fd(80)
        turt.bk(40)
        turt.right(90)
        turt.fd(40)
        turt.bk(80)
    

