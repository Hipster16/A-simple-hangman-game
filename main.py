import alphabet
import turtle
import words
import random
from tkinter import PhotoImage
from pynput import keyboard

screen = turtle.Screen()

screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
turtle.title("Hangman")

strs=""
initStr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keys=[]


def bg(file):
    background=PhotoImage(file=file).zoom(2,2)
    screen.addshape("background", turtle.Shape("image", background))
    tortoise = turtle.Turtle("background")
    tortoise.stamp()
    tortoise.hideturtle()

def initiate():
    x=-700
    y=200
    print(str)
    length=len(strs)
    a=turtle.Turtle()
    a.color("black")
    a.pensize(8)
    a.hideturtle()
    a.penup()
    a.setposition(x, y)
    for i in range(length):
        a.pendown()
        a.fd(50)
        a.penup()
        a.fd(20)
    a=turtle.Turtle()
    a.color("black")
    a.pensize(8)
    a.hideturtle()
    turtle.tracer(False)
    y=175
    for i in range(len(initStr)):
        if(i%7==0):
            offset=-700
            y-=90
        offset=x+(i%7)*90
        alphabet.letters(initStr[i], offset, y, "blue")
    a=turtle.Turtle()
    a.color("black")
    a.pensize(8)
    a.hideturtle()
    a.penup()
    a.setposition(200, -150)
    a.pendown()
    a.fd(400)
    a.bk(100)
    a.left(90)
    a.fd(500)
    a.left(90)
    a.fd(200)
    turtle.update()

def hang(a, i):
    turtle.tracer(True)
    if(i==0):
        a.penup()
        a.setpos(300 ,350)
        a.pendown()
        a.pensize(8)
        a.right(90)
        a.fd(110)
    elif(i==1):
        a.penup()
        a.setpos(270, 210)
        a.pendown()
        a.circle(30)
    elif(i==2):
        a.penup()
        a.setpos(300, 175)
        a.pendown()
        a.fd(130)
        a.bk(130)
    elif(i==3):
        a.left(45)
        a.fd(80)
        a.bk(80)
    elif(i==4):
        a.right(90)
        a.fd(80)
        a.bk(80)
        a.left(45)
    elif(i==5):
        a.fd(130)
        a.left(45)
        a.fd(80)
        a.bk(80)
    elif(i==6):
        a.right(90)
        a.fd(80)
        a.bk(80)
    turtle.tracer(False)    

def onPress(key):
    try:
        k = str(key).replace("'", "").upper()
        keys.insert(0, k)
        return False
    except AttributeError:
        print("Special key is pressed")

def locate(startX, startY, element,draw=True, tick=True):
    index=ord(element)-65
    y=startY-((index//7)*90)
    x=startX+(index%7)*90
    if tick: alphabet.letters("tick", x-7, y-80) 
    else: alphabet.letters("cross", x-12, y)

def display(ind, key):
    turtle.tracer(True)
    x=-690
    y=260
    for i in ind:
        offset=x+i*70
        alphabet.letters(key, offset, y)
    turtle.tracer(False)

def writeLine(strn, startX, startY, seperation, col="black"):
    offset=startX
    for i in strn:
        alphabet.letters(i, offset, startY, col)
        offset+=seperation-10

bg("ezgif.com-gif-maker.gif")
proceed=True
writeLine("HANGMAN", -270, 210, 70, "blue")
turtle.tracer(False)
writeLine("PRESS ENTER TO START", -600, 10, 70)
turtle.update()
while(True):
    with keyboard.Listener(
        on_press=onPress,
    ) as listener : listener.join()
    print(keys[0])
    if(keys[0]=="KEY.ENTER"):
        break
    keys.pop(0)

while(proceed):
    screen.clear()
    bg("ezgif.com-gif-maker.gif")
    strs=random.choice(words.words)
    strs=strs.upper() 
    length=len(strs)
    newstr="_"*length
    newstr=list(newstr)
    a=turtle.Turtle()
    a.hideturtle()
    print(strs)
    initiate()
    incorrect=0
    while(incorrect!=7):
        checker=[]
        while(True):
            with keyboard.Listener(
                on_press=onPress,
            ) as listener : listener.join()
            if(keys[0] in initStr):
                break
            keys.pop(0)
        if(keys.count(keys[0])>1):
            continue
        if(keys[0] in strs):
            for j in range(length):
                if(strs[j] == keys[0]):
                    checker.append(j)
                    newstr[j]=keys[0]
            locate(-700, 175, keys[0], True, True)
            turtle.update()
            display(checker, keys[0])
            if("_" not in newstr):
                break
        else:
            locate(-700, 85, keys[0], True, False)
            turtle.update()
            hang(a,incorrect)
            incorrect+=1
    screen.clear()
    bg("ezgif.com-gif-maker.gif")
    turtle.tracer(False)
    if(incorrect==7):
        print("lose")
        writeLine("YOU LOSE", -270, 280, 70, "red")
        writeLine("THE CORRECT WORD WAS ", -600, 190, 70)
        writeLine(strs, -250, 100, 70, "Blue")
    else:
        print("win")
        writeLine("YOU WIN", -270, 100, 70, "green")
    writeLine("WANNA PLAY AGAIN", -500, -20, 70)
    writeLine("ENTER        ESC", -500, -110, 70)
    turtle.update()
    while(True):
        with keyboard.Listener(
            on_press=onPress,
        ) as listener : listener.join()
        print(keys[0])
        if(keys[0]=="KEY.ESC"):
            print("esc")
            proceed=False
            break
        elif(keys[0]=="KEY.ENTER"):
            print("Enter")
            break
        keys.pop(0)
    keys=[]
    turtle.tracer(True)

turtle.bye()
