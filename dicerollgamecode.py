import random

vidas = {"vidasj1": 50, "vidasj2": 50}
turnos = {"dadoj1": 0, "dadoj2": 0}
jug_1 = {'atqj1': 0, 'defj1': 0}
jug_2 = {'atqj2': 0, 'defj2': 0}

while True:
    print("Tiren el dado para determinar quien ataca y quien defiende")
    print("El numero mayor ataca. Si caen lo mismo repiten")
    dice_roll_1 = input("J1 tira dados: ")
    dice_roll_2 = input("J2 tira dados: ")
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    turnos['dadoj1'] = dice_roll_1
    turnos['dadoj2'] = dice_roll_2
    print(turnos)

    if dice_roll_1 == dice_roll_2:
        print("Empate, tiren de nuevo")
        continue
    elif dice_roll_1 > dice_roll_2:
        print("j1 ataca y j2 defiende")
        atq = input("atacante tira dados: ")
        defensa = input("defensa tira dados: ")
        atq = random.randint(1, 6)
        jug_1['atqj1'] = atq
        defensa = random.randint(1, 6)
        jug_2['defj2'] = defensa
        if jug_1['atqj1'] > jug_2['defj2']:
            print("Le rompiste la defensa!")
            vidas['vidasj2'] = vidas['vidasj2'] - 10
            print("Te quieron -10 de vida!")
            print(f"Te queda {vidas['vidasj2']} de vida")
        elif jug_2['defj2'] > jug_1['atqj1']:
            print("Defendiste su ataque!")
            print("Contraataque!")
            vidas['vidasj1'] = vidas['vidasj1'] - 10
            print("Te quieron -10 de vida!")
            print(f"Te queda {vidas['vidasj1']} de vida")
        else:
            print("Igualaron poder!")
        print(jug_1)
        print(jug_2)
    else:
        print("j2 ataca y j1 defiende")
        atq = input("atacante tira dados: ")
        defensa = input("defensa tira dados: ")
        atq = random.randint(1, 6)
        jug_2['atqj2'] = atq
        defensa = random.randint(1, 6)
        jug_1['defj1'] = defensa
        if  jug_2['atqj2'] > jug_1['defj1']:
            print("Le rompiste la defensa!")
            vidas['vidasj1'] = vidas['vidasj1'] - 10
            print("Te quieron -10 de vida!")
            print(f"Te queda {vidas['vidasj1']} de vida")
        elif jug_1['defj1'] > jug_2['atqj2']:
            print("Defendiste su ataque!")
            print("Contraataque!")
            vidas['vidasj2'] = vidas['vidasj2'] - 10
            print("Te quieron -10 de vida!")
            print(f"Te queda {vidas['vidasj2']} de vida")
        else:
            print("Igualaron poder!")
        print(jug_1)
        print(jug_2)
    if vidas['vidasj1'] == 0:
        print(vidas)
        print("El jugador 2 ha ganado")
        break
    elif vidas['vidasj2'] == 0:
        print(vidas)
        print("El jugador 1 ha ganado")
        break
