import random

def lotto_game():
    sorsolt_szamok = []
    megadott_szamok = []
    print("Szevasz testvír! Látom szerencsejáték függő vagy. Sok sikert!")
    
    while len(megadott_szamok) < 5:
        try:
            jatekos_szamai = int(input(f"Adj meg egy számot (1-90), eddigiek: {megadott_szamok}: "))
            if jatekos_szamai < 1 or jatekos_szamai > 90:
                print("A számnak 1 és 90 között kell lennie!")
            elif jatekos_szamai in megadott_szamok:
                print("Már megadtad ezt a számot.")
            else:
                megadott_szamok.append(jatekos_szamai)
        except ValueError:
            print("Érvényes számot adj meg!")
    
    print(f"A megadott számaid: {megadott_szamok}")
    
    while len(sorsolt_szamok) < 5:
        gep_szamai = random.randint(1, 90)
        if gep_szamai not in sorsolt_szamok:
            sorsolt_szamok.append(gep_szamai)
    
    print(f"A sorsolt számok: {sorsolt_szamok}")
    
    talalatok = len(set(megadott_szamok) & set(sorsolt_szamok))
    print(f"Találatok száma: {talalatok}")

lotto_game()
