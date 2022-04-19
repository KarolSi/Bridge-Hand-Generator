import random as rd
import turtle 

SPos = turtle.Vec2D(-50, -150)
NPos = turtle.Vec2D(-50, 150)
WPos = turtle.Vec2D(-150,50)
EPos = turtle.Vec2D(150, 50)

def writing(pla):
    
    for i in range(len(pla["1"])):
        print(pla["1"][i], end=" ")
    print("")
    
    for i in range(len(pla["2"])):
        print(pla["2"][i], end=" ")
    print("")
    
    for i in range(len(pla["3"])):
        print(pla["3"][i], end=" ")
    print("")
    
    for i in range(len(pla["4"])):
        print(pla["4"][i], end=" ")

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
    N = {'1': ["♠ "],'2': ["♥ "], '3': ["♦ "], '4': ["♣ "]}
    E = {'1': ["♠ "],'2': ["♥ "], '3': ["♦ "], '4': ["♣ "]}
    S = {'1': ["♠ "],'2': ["♥ "], '3': ["♦ "], '4': ["♣ "]}
    W = {'1': ["♠ "],'2': ["♥ "], '3': ["♦ "], '4': ["♣ "]}
    cards = [" ","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A"]

    for i in range(0,13):
        draw(N)
        draw(S)
        draw(E)
        draw(W)
    writing(N)
    
    
    

    
    