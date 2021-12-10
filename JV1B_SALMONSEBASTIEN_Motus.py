import random

from colorama import init
from colorama import Fore, Back, Style

#variables

wordList = ["citron","carrée","plumer","orages","oiseau","moulin","poulet","orange","cinema","marche","ouvrir","peuple","couler","cypres","border","billes","argent","boules","achats","annule","alunir","amener","poires","pommes","tables","taupes","sabler","posees","parler","tester"]
attempts = 8 #Nombres de tentatives accorder aux joueurs.ses
gameOver = False
drawnWord = wordList[random.randint(0,(len(wordList)))]
        


#Affiche la proposition et identifie quelles lettres sont bien / mal placées
def displayProposition (word, wordProposition):
    for i in range (len(word)):
        if wordProposition[i] == word[i]:
            print(Fore.RED + wordProposition[i]) 
        
        else:
            print(Fore.BLUE + wordProposition[i]) 

#Lance un nouveau tour tant que la victoire ou la défaite ne sont pas atteintes
def newTurn ():

    print ("Un mot vient d'être tiré au sort, à vous de le deviner")
    wordProposition = input("Quel mot ? ")

    displayProposition(drawnWord,wordProposition)

    attempts -= 1

    return newTurn


#Vérifie si la victoire est atteinte ou non 
def victoryCheck (word, wordProposition):
    
    if wordProposition == word:
        print ("Vous avez gagné !")
        exit()

    else:
        newTurn

#Vérifie si une lettre est présente mais mal placée (pas fonctionnelle)
def wrongPlace(word, wordProposition,letter):
    position = 0
    for i in range (len(word)):
        if word [i] == letter:
            print(Fore.YELLOW + wordProposition[i])


            return wrongPlace

#Vérifie si une lettre est présente mais mal placée (pas fonctionnelle)
def positionLetter (word, position, letter):
    position = 0
    for i in range (len(word)):
        if word [i] == letter:
            position = word[i]
            print(Fore.YELLOW + letter)
                                



#Turn 1

wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)


print ("Il vous reste", attempts, "tentatives.")


#Turn 2


wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)


print ("Il vous reste", attempts, "tentatives.")


#Turn 2


wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)

print ("Il vous reste", attempts, "tentatives.")


#Turn 3


wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)

print ("Il vous reste", attempts, "tentatives.")

#Turn 4


wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)

print ("Il vous reste", attempts, "tentatives.")


#Turn 5


wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)

print ("Il vous reste", attempts, "tentatives.")


#Turn 6

wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)

print ("Il vous reste", attempts, "tentatives.")



#Turn 7

wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)

attempts -= 1


print(Style.RESET_ALL)
print ("Il vous reste", attempts, "tentatives.")

#Turn 8

wordProposition = input("Quel mot ? ")

displayProposition(drawnWord,wordProposition)

victoryCheck(drawnWord,wordProposition)


print(Style.RESET_ALL)

print ("Vous n'avez pas réussi à trouver le mot mystère !")

