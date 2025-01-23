import math
import random 
from words import words as w
from pendu import *


word = ""
tulpe_letter = []
blank_word = []
print_blank_word = ""

print(math.ceil(random.random()*10))

print(""" 
==========================================
!                                        !     
!                                        !
!       ~~~~ LE JEUX DU PENDU ~~~~       !
!                                        !
!                                        !      
==========================================

""")



# Definir une fonction pour choisir un mot au hasard dans le dictionnaire ou la liste presente dans words.py ou fichier json

def get_word() :
    index = (math.ceil(random.random()*len(w)-1))
    selected_word = w[index]
    return selected_word

# Prendre le mot et le changer en dictionnaire ou en  tulpe grace au set, pour attribuer la valeur false à chaque lettre du mot

def set_word_for_game() :
    global word
    global tulpe_letter
    word = get_word().lower()
    tulpe_letter = [(letter, False) for letter in word]
    tulpe_letter = set(tulpe_letter)
    hide_or_show_letter(word, tulpe_letter)
    


# Initialiser le mot avec des _ si la lettre est à false

def hide_or_show_letter(word, tulpe_letter): 
   global blank_word
   blank_word = [] 
   for letter in word:
      for tulpe in tulpe_letter:
         if letter == tulpe[0] and tulpe[1] == False:
            letter_temp = "_"
            blank_word += letter_temp  
         elif letter == tulpe[0] and tulpe[1] == True:
            letter_temp = tulpe[0]
            blank_word += tulpe[0]
   print_word()

# 1\ recuperer le mot et le tulpe et pour chaque lettre dans le mot, il faut verifier si la lettre correspondante est True ou False dans le tulpe, je dois retourner mot blank _ 
# Si il y a une entrée user, la tester avec la fonction compare_letter


# ici à la place de juste cacher je devrais pouvoir cacher ou montrer selon si le tulpe est True ou False selon l'entrée user (mais si je fais ça je ne peux pas l'initialiser en premier lieu sauf si je lui met un parametre par defaut)

def print_word() :
   word = ""
   for letter in blank_word :
      word += letter
   print(word)

# Fonction pour comparer l'entré avec
def compare_letter(user_letter):
   global tulpe_letter
   find_tulpe_letter = [tulpe for tulpe in tulpe_letter if tulpe[0] == user_letter]
   if len(find_tulpe_letter) > 0 and find_tulpe_letter[0][1] != True:
      tulpe_letter.remove((user_letter, False))
      new_entrie = (user_letter, True)
      tulpe_letter.add(new_entrie)
      return True
   elif len(find_tulpe_letter) > 0 and find_tulpe_letter[0][1] == True: 
      print("Vous avez deja cette lettre")
   else:
     print("Cette lettre n'existe pas")
   


# Faire une entrer utilisateur 
def get_letter_from_user():
   i=6
   while i >= 0:
    print(print_blank_word)
    user_letter = input("Entrez une lettre. ").lower()
    if len(user_letter) > 1:
       print(f"Non vous devez entrez qu'une seule lettre : tentative restante {i}")
    elif user_letter.isdigit():
       print(f"Non vous devez entrez une seule lettre pas un chiffre : tentative restante {i}")
    else:
      # On a bien une lettre valide donc :
      # 1/je compare la lettre 
      letter_exist = compare_letter(user_letter)
      print(letter_exist)
      if letter_exist: 
         hide_or_show_letter(word, tulpe_letter)
       
       # Fonction qui compare 
       
       
          
       


# Parametre du jeu
def main() :
   # initialise le mot
   set_word_for_game()
   # Recupere les tentatives de l'utilisateur 
   get_letter_from_user()



# on lance le programme
main()