import random as rd
import turtle


SPos = turtle.Vec2D(-50,-100)
NPos = turtle.Vec2D(-50, 150)
WPos = turtle.Vec2D(-120,50)
EPos = turtle.Vec2D(100, 50)

def writing(pos, pla):
    global p, ki, ka, t, NPos
    p = "♠ "
    ki = "♥ "
    ka = "♦ "
    t = "♣ "
    colors = [" ",p,ki,ka,t]
    for key in range(1,5):
        
        for i in range(len(pla[str(key)])):
                colors[key] += (pla[str(key)][i])
                colors[key] += " "
        writer.goto(pos)
        print(pos[1])
        pos -= turtle.Vec2D(0,20)
        print(colors[key])
        writer.write(colors[key])

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


print("ile rozdań rozdać?")
roz = int(input("<<"))

for i in range(roz):
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
    ht = int(input("<<<"))
        
    


    
    