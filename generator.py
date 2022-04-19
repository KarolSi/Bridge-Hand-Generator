import random as rd

def wypisanie(zawo):
    print('N:')
    print("     ♠ ", end=" ")
    for i in range(len(zawo["1"])):
        print(zawo["1"][i], end=" ")
    print("")
    print("     ♥ ", end=" ")
    for i in range(len(zawo["2"])):
        print(zawo["2"][i], end=" ")
    print("")
    print("     ♦ ", end=" ")
    for i in range(len(zawo["3"])):
        print(zawo["3"][i], end=" ")
    print("")
    print("     ♣ ",end = " ")
    for i in range(len(zawo["4"])):
        print(zawo["4"][i], end=" ")


def losowanie(zawodnik):
        global zaw 
        zaw = zawodnik
        kolor = rd.randint(0,3)
        karta = rd.randint(1,13)

        if(karty[karta+13*kolor]!='#'):
            zawodnik[str(kolor+1)].append(karty[karta+(13*kolor)])
            karty[karta+13*kolor] = '#'
        
            return 0
        else:
            losowanie(zaw)



print("ile rozdań rozdać?")
roz = int(input("<<"))

for i in range(roz):
    N = {'1': [],'2': [], '3': [], '4': []}
    E = {'1': [],'2': [], '3': [], '4': []}
    S = {'1': [],'2': [], '3': [], '4': []}
    W = {'1': [],'2': [], '3': [], '4': []}
    karty = [" ","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A","2","3","4","5","6","7","8","9","T","J","Q","K","A"]

    for i in range(0,13):
        losowanie(N)
        losowanie(S)
        losowanie(E)
        losowanie(W)
    wypisanie(N)
    

    
    