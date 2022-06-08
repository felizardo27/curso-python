
def jogar():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    palavra = list()
    for p in range(len(palavra_secreta)):
        palavra.append("_")
    
    while not acertou and not  enforcou:
        chute = input("Qual letra? ").strip(" ")
        
        for i, letra in enumerate(palavra_secreta):
            if letra.upper() == chute.upper():
                print(f"Encontrei a letra {letra} na posicao {i}")
                palavra[i] = chute
                
        print("jogando...")
            
        for p in palavra:
            print(p, end="")
        print()
            
    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()