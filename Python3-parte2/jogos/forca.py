import random
import os
import platform
from time import sleep

def clear():
    sleep(0.2)
    if platform.system().upper() == "WINDOWS":
        os.system("cls")
    if platform.system().upper() == "LINUX":
        os.system("clear")

def imprime_mensagem_abertura():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = list()
    
    for linha in arquivo:
        palavras.append(linha.strip())
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def imprimi_letras_acertadas(letras):
    print()
    for l in letras:
        print(l, end=" ")
    print('\n')

def pede_chute():
    return input("Qual letra? ").strip().upper()

def verificar_chute(chute, acertadas, palavra):
    for i, letra in enumerate(palavra):
            if  chute == letra:
                acertadas[i] = chute

def imprimi_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def imprimi_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |     (º_º)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |     (º_º)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |     (º_º)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |     (º_º)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |     (º_º)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |     (º_º)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |     (º_º)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def jogar():
    
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    imprimi_letras_acertadas(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    
    while(not enforcou and not acertou):

        chute = pede_chute()
        
        clear()

        if chute in palavra_secreta:
            verificar_chute(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        imprimi_letras_acertadas(letras_acertadas)


    if acertou:
        imprimi_mensagem_vencedor()
    if enforcou:
        imprimi_mensagem_perdedor(palavra_secreta)


if(__name__ == "__main__"):
    jogar()
