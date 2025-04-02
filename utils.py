def escolha_usuario():
    opcoes = {1: 'pedra', 2: 'papel', 3: 'Tesoura'}

    while True: #loop no menu de escolha 
        print("\nEscolha sua jogada: ")
        print("1- Pedra") 
        print("2- Papel")
        print("3- Tesoura")
        try:
            escolha = int(input("Digite o número que deseja escolher: ").strip())
            if escolha in opcoes:
                return opcoes[escolha]  #retorna a jogada desse filho da puta
            else:
                print("Opção inválida! Tente outra vez.")
        except ValueError:
            print("Entrada inválida! Digite um número de 1 a 3.") #tudo tem que tratar nessa bosta
def vencedor(usuario, computador):
    usuario = usuario.lower() 
    computador = computador.lower()
    
    regras = {
        "pedra": 'tesoura',
        "papel": 'pedra',  # legal python é chave dms 
        "tesoura": 'papel'
    }

    if regras[usuario] == computador:
        return "Você venceu!! "
    else:
        return "O computador Venceu!!"
    
def exibeRegras():
    print("\n=== Regras do JOGO ===")
    print("📌 Pedra ganha de Tesoura") # desnecessario mas legal dmskkkkkkk
    print("📌 Tesoura ganha de Papel")
    print("📌 Papel ganha de Pedra")
    print("📌 Se ambos escolherem a mesma opção, EMPATE!! ")