import random
from typing import final

def dn(many,sides):
    moreDices = 0
    dices = list()
    for qtd in range(0,many):
        diceRnd = random.randint(1, sides)
        moreDices = moreDices + diceRnd
        dices.append(diceRnd)
        if sides == 20:
            if diceRnd == 20:
                print("VINTE NATURAL!!! BOTA PRA QUEBRAR!")
    print("Os resultados dos dados foram:",dices)
    return moreDices

def jogar():
    quest = input("Olá, bravo jogador! Quantos dados você deseja lançar?")
    quant = int(quest)
    diceChoiceSTR = input("De quantos lados é o dado que você deseja jogar?")
    diceChoice = int(diceChoiceSTR)
    if quant == 0:
        print("Jogador, você não digitou um valor válido para a quantidade de dados! Você não irá para valhalla! Sike, pode mandar outro valor!")
        jogar()
    else:
        if diceChoice == 0:
            print("Você não sabia que 0 vezes qualquer coisa é zero? Joga de novo")
            jogar()
        else:
            y = dn(quant, diceChoice)
            print("A soma total dos dados lançados é de:", y)
jogar()

