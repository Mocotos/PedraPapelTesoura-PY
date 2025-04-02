from game import *
from utils import *


def menu():
    while True:
        print("=== MENU STONE/PAPER/SCISOR ===") # ficou legal o codigo do menu so faltou cores
        print("1- Jogar")
        print("2- Regras") 
        print("3- Sair")

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            jogar()
        elif escolha == '2':
            exibeRegras()
        elif escolha == '3':
            print('Saindo do jogo...')
            break
        else:
            print("Opção Inválida! tente novamente! ")

if __name__ == "__main__":
    menu() # deixei jogar() e caçei o erro do menu por 30 minutos