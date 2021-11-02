import random
from typing import final

def diceFunc():
    dices = list()
    finalDices = 0
    diceCountSTR = input("Quantos dados você deseja rolar?")
    diceCount = int(diceCountSTR)
    diceChoice = input("Qual dado você deseja rolar? D6 ou D20?")
    if(diceChoice == "D6" or "d6" or "6"):
        list1 = [1,2,3,4,5,6]
        for diceCount in list1:
            diceRnd = random.choice(list1)
            dices.append(diceRnd)
        finalDices = sum(dices)
        print("O valor final é: ", finalDices)
        print("Os dados rolados foram:", dices)      
    elif(diceChoice == "D20" or "d20" or "20"):
        list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        for diceCount in list1:
            diceRnd = random.choice(list1)
            dices.append(diceRnd)
        finalDices = sum(dices)
        print("O valor final é: ", finalDices)
        print("Os dados rolados foram:", dices)   
    else:
        print("Você não digitou um dado válido, tente novamente")
        diceFunc()
    


diceFunc()