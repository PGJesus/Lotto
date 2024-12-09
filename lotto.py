import random

def lotto_game():
    sorsolt_szamok = []
    megadott_szamok = []
    x = 0
    print("Szevasz testvír! Látom szerencsejáték függő vagy. Sok sikert!")
    while x < 5:
        jatekos_szamai = int(input("Mondj öt különböző számot!"))
        if jatekos_szamai in megadott_szamok:
            print("Már megadtad ezt a számot.")
        else:
            megadott_szamok.append(jatekos_szamai)
            x += 1    
    print(megadott_szamok)
    for i in range(0, 5):
        gep_szamai = random.randint(1, 90)
        sorsolt_szamok.append(gep_szamai) 
    print(sorsolt_szamok)
    
    talalatok = 0
    if megadott_szamok in sorsolt_szamok:
        talalatok + 1 
    print(talalatok)
lotto_game()