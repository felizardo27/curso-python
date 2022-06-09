
def jogar():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

    palavra_secreta = "banana".upper()
    enforcou = False
    acertou = False
    erros = 0

    palavra = ["_" for letra in palavra_secreta]
    
    
    for p in palavra:
        print(p, end=" ")
    print()
    
    while not acertou and not  enforcou:
        
        chute = input("Qual letra? ").strip().upper()
        
        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    palavra[i] = chute
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in palavra
        
        for p in palavra:
            print(p, end=" ")
        print()
            
    if acertou:
            print("Você ganhou!!")
    if enforcou:
        print("Você perdeu!!")
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()