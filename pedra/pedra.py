import random
class pedra():
    def __init__(self):
        pc = random.randrange(1, 3)
        vc = int(input("Qual sua escolha?\n1-pedra\n2-papel\n3-tesoura\nR: "))
        print("---------------------")
        if pc == 1:
            print("PC: pedra")
        elif pc == 2:
            print("PC: papel")
        else:
            print("PC: tesoura")
        if vc == 1:
            print("Você: pedra")
        elif vc == 2:
            print("Você: papel")
        else:
            print("Você: tesoura")
        if vc == 1:
            if pc == 1:
                print("Empatou")
            elif pc == 2:
                print("Perdeu")
            else:
                print("Ganhou")
        elif vc == 2:
            if pc == 1:
                print("Ganhou")
            elif pc == 2:
                print("Empatou")
            else:
                print("Perdeu")
        else:
            if pc == 1:
                print("Perdeu")
            elif pc == 2:
                print("Ganhou")
            else:
                print("Empatou")
        print("---------------------")