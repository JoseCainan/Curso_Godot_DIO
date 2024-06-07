op = -1
while op != 0:
    nome = input("Informe o nome do heroi")
    XP_hero = float(input("informe o xp do seu heroi"))

    if XP_hero <= 1000:
        print("O heroi de nome {} está no nível FERRO".format(nome))

    elif 1001 <= XP_hero <= 2000:
        print("O heroi de nome {} está no nível BRONZE".format(nome))

    elif 2001 <= XP_hero <= 5000:
        print("O heroi de nome {} está no nível PRATA".format(nome))

    elif 5001 <= XP_hero <= 7000:
        print("O heroi de nome {} está no nível OURO".format(nome))

    elif 7001 <= XP_hero <= 8000:
        print("O heroi de nome {} está no nível PLATINA".format(nome))

    elif 8001 <= XP_hero <= 9000:
        print("O heroi de nome {} está no nível ASCENDENTE".format(nome))

    elif 9001 <= XP_hero <= 10000:
        print("O heroi de nome {} está no nível IMORTAL".format(nome))

    elif XP_hero >= 10001:
        print("O heroi de nome {} está no nível RADIANTE".format(nome))

    print("---------------Menu------------------\n")
    print("|1- Classificar outro heori|" 
          "|0- Sair do programa       |")
    op = int(input("Escolha uma opção: "))