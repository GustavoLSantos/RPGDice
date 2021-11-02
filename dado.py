import random
from typing import final

def d6(number):
    moreDices = 0
    for qtd in range(0,number):
        diceRnd = random.randint(1, 6)
        moreDices = moreDices + diceRnd
    return moreDices

def d20(number):
    moreDices = 0
    for qtd in range(0,number):
        diceRnd = random.randint(1,20)
        moreDices = moreDices + diceRnd
        if diceRnd == 20:
            print("Um vinte natural!")
            return moreDices
    return moreDices

def d10(number):
    moreDices = 0
    for qtd in range(0,number):
        diceRnd = random.randint(1,10)
        moreDices = moreDices + diceRnd
    return moreDices

def jogar():
    quest = input("Olá, bravo jogador! Quantos dados você deseja lançar?")
    quant = int(quest)
    diceChoice = input("E qual dado você quer jogar no campo de batalha? D6, D10 ou D20?")
    if diceChoice == "D6":
        y= d6(quant)
        print(y)
    elif diceChoice =="D10":
        y = d10(quant)
        print(y)
    elif diceChoice == "D20":
        y = d20(quant)
        print(y)
    else:
        print("Você não digitou um dado válido, caro player! VOCÊ NÃO IRÁ PARA VALHALLA!!! Sike, tente novamente!")
        jogar()

jogar()

