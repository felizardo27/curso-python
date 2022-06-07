print('-'*32)
print("Bem vindo ao jogo de Adivinhação")
print('-'*32)

numero_secreto = 42
total_de_tentativas = 3

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
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


print("Fim de jogo!")
