from pedra import pedra
escolha = int(input("Quer jogar pedra papel tesoura?\n1-SIM\n2-NÃO\nR: "))
while escolha == 1:
    pedra()
    escolha = int(input("Quer continuar jogando?\n1-SIM\n2-NÃO\nR: "))