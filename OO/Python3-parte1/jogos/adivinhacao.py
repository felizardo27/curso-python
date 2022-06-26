from random import randint

def jogar():
    print('-'*32)
    print("Bem vindo ao jogo de Adivinhação")
    print('-'*32)

    numero_secreto = randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil / (2) Médio / (3) Difício")


    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print('Nível inválido')


    for rodada in range(total_de_tentativas):
        print(f"Tentativa {rodada+1} de {total_de_tentativas}")
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print(f"Você digitou {chute_str}")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f"Você acertou! e fez {pontos} pontos")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"Fim de jogo! o Número secreto era {numero_secreto}")

if __name__ == "__main__":
    jogar()