import random
from utils import escolha_usuario, vencedor


def jogar(): # all pra joga
    opcoes = ["pedra", "papel", "tesoura"]

    usuario = escolha_usuario()
    computador = random.choice(opcoes)

    print(f"\nVocê escolheu: {usuario}")
    print(f"\nO computador escolheu: {computador}")

    resultado = vencedor(usuario, computador)
    print(resultado)