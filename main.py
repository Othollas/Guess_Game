import math
import random 
from words import words as w
from pendu import *

# Variables globales pour gérer l'état du jeu
word = ""  # Le mot mystère à deviner
tulpe_letter = []  # Liste des lettres sous forme de tuples avec leur état (trouvé ou non)
blank_word = []  # Représentation actuelle du mot avec les lettres trouvées et les underscores
i = 10  # Nombre de tentatives restantes

# Bannière du jeu affichée au démarrage
print(""" 
==========================================
!                                        !     
!                                        !
!       ~~~~ LE JEUX DU PENDU ~~~~       !
!                                        !
!                                        !      
==========================================
""")

# Fonction pour choisir un mot au hasard dans la liste
def get_word():
    index = (math.ceil(random.random() * len(w) - 1))  # Sélectionne un index aléatoire
    selected_word = w[index]  # Récupère le mot correspondant
    return selected_word

# Prépare le mot choisi pour le jeu, avec chaque lettre marquée comme "non trouvée"
def set_word_for_game():
    global word
    global tulpe_letter
    word = get_word().lower()  # Convertit le mot en minuscules pour éviter les erreurs de casse
    tulpe_letter = [(letter, False) for letter in word]  # Crée des tuples (lettre, False)
    tulpe_letter = set(tulpe_letter)  # Utilise un set pour éviter les doublons
    hide_or_show_letter(word, tulpe_letter)  # Met à jour l'affichage initial

# Gère l'affichage du mot avec des underscores pour les lettres non trouvées
def hide_or_show_letter(word, tulpe_letter):
    global blank_word
    blank_word = []  # Réinitialise l'affichage
    for letter in word:
        for tulpe in tulpe_letter:
            if letter == tulpe[0] and tulpe[1] == False:  # Lettre non trouvée
                blank_word.append("_")
            elif letter == tulpe[0] and tulpe[1] == True:  # Lettre trouvée
                blank_word.append(tulpe[0])

# Compare la lettre entrée par l'utilisateur avec celles du mot mystère
def compare_letter(user_letter):
    global tulpe_letter
    global i
    find_tulpe_letter = [tulpe for tulpe in tulpe_letter if tulpe[0] == user_letter]
    if len(find_tulpe_letter) > 0 and find_tulpe_letter[0][1] != True:
        # Lettre correcte et pas encore utilisée
        tulpe_letter.remove((user_letter, False))
        tulpe_letter.add((user_letter, True))  # Marque la lettre comme trouvée
        return True
    elif len(find_tulpe_letter) > 0 and find_tulpe_letter[0][1] == True:
        # Lettre déjà utilisée
        print("Vous avez déjà entré cette lettre")
    else:
        # Lettre incorrecte
        print("Cette lettre n'est pas dans le mot")
        i -= 1  # Réduit le nombre de tentatives restantes

# Affiche le mot mystère avec les lettres trouvées et les underscores
def print_word():
    word = "".join(blank_word)
    print(f"""
         Tentatives restantes : {i}

               {word}
         
         """)

# Affiche l'état actuel du pendu en fonction des tentatives restantes
def print_pendu():
    pendu = {0: pendu0, 1: pendu1, 2: pendu2, 3: pendu3, 4: pendu4, 5: pendu5, 6: pendu6}
    if i < 10:
        print(pendu[i])

# Vérifie les conditions de victoire ou de défaite
def victory_of_defeat():
    if i == 0:  # Joueur perd
        print(f"""
               Le mot était : {word}
      """)
        continue_or_exit()
    else:
        list_true = [True for tulpe in tulpe_letter if tulpe[1] == True]
        if len(list_true) == len(tulpe_letter):  # Joueur gagne
            print("""
               Vous avez gagné !
               """)
            continue_or_exit()

# Permet au joueur de rejouer ou de quitter le jeu
def continue_or_exit():
    again = input("Voulez-vous continuer O/N ? ").lower()
    while again not in ("o", "n"):
        print("Choisissez O ou N (majuscule ou minuscule) !!")
        again = input("Voulez-vous continuer O/N ? ").lower()
    if again == "o":
        main()
    elif again == "n":
        exit()

# Boucle principale du jeu pour gérer les entrées utilisateur et l'affichage
def game():
    global i
    i = 6  # Réinitialise les tentatives à chaque partie
    while i >= 0:
        print_word()
        user_letter = input("Entrez une lettre. ").lower()
        if len(user_letter) > 1:
            print(f"Non, vous devez entrer une seule lettre : tentatives restantes {i}")
        elif user_letter.isdigit():
            print(f"Non, vous devez entrer une lettre, pas un chiffre : tentatives restantes {i}")
        else:
            if compare_letter(user_letter):  # Mise à jour des lettres trouvées
                hide_or_show_letter(word, tulpe_letter)
        print_pendu()
        victory_of_defeat()

# Initialisation et lancement du jeu
def main():
    set_word_for_game()  # Prépare le mot
    game()  # Lance la partie

# Point d'entrée du programme
main()
