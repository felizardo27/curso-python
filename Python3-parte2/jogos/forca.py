import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r", encoding="utf-8")
    
    palavras = list()
    
    for linha in arquivo:
        palavras.append(linha.strip())
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_acertadas[i] = chute
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!!")
    if enforcou:
        print(f"Você perdeu!! A palavra era {palavra_secreta}")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
