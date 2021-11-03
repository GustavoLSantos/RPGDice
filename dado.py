import random
from typing import final

# Escolha de idioma / Language choose
def language():
    lang = input("Escolha a língua / Choose your Language: Port ou Eng  ")
    if lang == "Port":
        jogar()
    elif lang == "Eng":
        play()
    else:
        print("Você não escolheu um valor válido, tente novamente!")
        print("You didn't type a valid value, try again")
        language()
    
#English
def dnEng(many,sides):
    moreDices = 0
    dices = list()
    for qtd in range(0,many):
        diceRnd = random.randint(1, sides)
        moreDices = moreDices + diceRnd
        dices.append(diceRnd)
        if sides == 20:
            if diceRnd == 20:
                print("NATURAL 20!! BREAK A LEG!")
    print("The dice results are: ",dices)
    return moreDices

def play():
    quest = input("Hello, mighty player! How many dices do you wanna launch?")
    quant = int(quest)
    diceChoiceSTR = input("And how many sides these dices haves?")
    diceChoice = int(diceChoiceSTR)
    if quant == 0:
        print("Player, you didn't type a valid amount of dices! You're not worthy of valhalla! Sike, shoot another amount!")
        play()
    else:
        if diceChoice == 0:
            print("Don't you know that 0 times ANYTHING is ZERO? Play again")
            play()
        else:
            y = dn(quant, diceChoice)
            print("The sum of the launched dices is:", y)

#Português
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

language()

