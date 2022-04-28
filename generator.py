import random as rd
from turtle import Screen
import turtle


SPos = turtle.Vec2D(-50,-120)
NPos = turtle.Vec2D(-50, 160)
WPos = turtle.Vec2D(-240,30)
EPos = turtle.Vec2D(110, 30)
comp = {"♣": 1, "♦": 1, "♥": 1, "♠": 1," ":2, "A": 3, "K": 4, "Q": 5,"J": 6,"T": 7,"9": 8,"8": 9, "7": 10, "6": 11, "5": 12,"4":13,"3":14,"2":15}

def writing(pos, pla):
    global p, ki, ka, t, NPos, comp
    p = "♠"
    ki = "♥"
    ka = "♦"
    t = "♣"
    colors = [" ",p,ki,ka,t]
    for k in range(1,5):
        hand = ""
        
        for i in range(1,len(pla[str(k)])):
                colors[k] += (pla[str(k)][i])
                
                
        writer.goto(pos)
        pos -= turtle.Vec2D(0,25)
        colors[k] = sorted(colors[k], key=comp.get)
        print(colors[k])

        for i in range(len(colors[k])):
            hand += colors[k][i]
            hand += " "

        writer.write(hand, font=("Courier", 14, "bold"))
    print(" ")

def draw(player):
        global zaw 
        zaw = player
        color = rd.randint(0,3)
        karta = rd.randint(1,13)

        if(cards[karta+13*color]!='#'):
            player[str(color+1)].append(cards[karta+(13*color)])
            cards[karta+13*color] = '#'
        
            return 0
        else:
            draw(zaw)

def deal(x, y):
    writer.clear()
    global cards
    N = {'1': [" "],'2': [" "], '3': [" "], '4': [" "]}
    E = {'1': [" "],'2': [" "], '3': [" "], '4': [" "]}
    S = {'1': [" "],'2': [" "], '3': [" "], '4': [" "]}
    W = {'1': [" "],'2': [" "], '3': [" "], '4': [" "]}
    cards = [" ","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A"]

    for i in range(0,13):
        draw(N)
        draw(S)
        draw(E)
        draw(W)


    writing(WPos, W)
    writing(EPos, E)
    writing(NPos, N)
    writing(SPos, S)
    

#Window setting
wn = turtle.Screen()
wn.title("Bridge Hands Generator")
wn.bgcolor('white')
wn.register_shape('nesw.gif')


#Shape setting
nesw = turtle.Turtle()
nesw.up()
nesw.setpos(turtle.Vec2D(0, 0))
nesw.shape('nesw.gif')


#Writer setting
writer = turtle.Turtle()
writer.up()
writer.ht()


#button setting
button = turtle.Turtle()
button.hideturtle()
button.shape('square')
button.shapesize(1,3)
button.fillcolor('red')
button.penup()
button.setpos(100,-240)
button.write("Deal!", align='center', font=20)
button.showturtle()
button.setpos(100, -250)
button.onclick(deal)
screen = Screen()
screen.mainloop()





        
    


    
    