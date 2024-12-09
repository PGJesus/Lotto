import random

def lotto_game():
    sorsolt_szamok = []
    megadott_szamok =[]
    print("Szevasz testvír! Látom szerencsejáték függő vagy. Sok sikert!")
    for i in range(0,5):
        jatekos_szamai = int(input("Mondj öt különböző számot!"))
        megadott_szamok.append(jatekos_szamai)
    print(megadott_szamok)
        # if :
        #     print("Már megadtad ezt a számot bazzeg há nem tudsz olvasni")
    for i in range(0, 5):
        gep_szamai = random.randint(1, 90)
        sorsolt_szamok.append(gep_szamai)
    print(sorsolt_szamok)
    
    
lotto_game()