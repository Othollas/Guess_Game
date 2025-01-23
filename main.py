import math
import random 
from words import words as w
from pendu import *


word = ""
tulpe_letter = []
blank_word = []
i=10

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
   

# Fonction pour comparer l'entré avec
def compare_letter(user_letter):
   global tulpe_letter
   global i
   find_tulpe_letter = [tulpe for tulpe in tulpe_letter if tulpe[0] == user_letter]
   if len(find_tulpe_letter) > 0 and find_tulpe_letter[0][1] != True:
      tulpe_letter.remove((user_letter, False))
      new_entrie = (user_letter, True)
      tulpe_letter.add(new_entrie)
      return True
   elif len(find_tulpe_letter) > 0 and find_tulpe_letter[0][1] == True:
      print("Vous avez deja entré cette lettre")
   else:
      print("Cette lettre n'est pas dans le mot")
      i -= 1
     



def print_word() :
   word = ""
   for letter in blank_word :
      word += letter
   print(f"""
         Tentavive restante : {i}

               {word}
         
         """)


def print_pendu():
   pendu = {0 : pendu0, 1 : pendu1, 2 : pendu2, 3 : pendu3, 4 : pendu4, 5 : pendu5, 6 : pendu6}
   if i<10:
      print(pendu[i])





def victory_of_defeat():
   if (i == 0):     
      print(f"""
         
               Le mot était : {word}

      """)
      
      continue_or_exit()

   else:
      list_true = [True for tulpe in tulpe_letter if tulpe[1] == True]
      list_letter = len(tulpe_letter)
      if len(list_true) == list_letter:
         print("""
               
               Vous avez gagnez 
               
               """)
         continue_or_exit()

def continue_or_exit():
   again = input("Voulez nous continuer O/N ? ").lower()
   while again != "o" and again != "n":
      print("Choisissez O ou N (majuscule ou minuscule)!!")
      again = input("Voulez nous continuer O/N ? ").lower()
   if again == "o":
      main()
   elif again == "n":
      exit()
      

# Faire une entrer utilisateur 
def game():
   global i
   i=6
   while i >= 0:
      print_word()
      user_letter = input("Entrez une lettre. ").lower()
      if len(user_letter) > 1:
         print(f"Non vous devez entrez qu'une seule lettre : tentative restante {i}")
      elif user_letter.isdigit():
         print(f"Non vous devez entrez une seule lettre pas un chiffre : tentative restante {i}")
      else: 
         letter_exist = compare_letter(user_letter)
         print(letter_exist)
         if letter_exist: 
            hide_or_show_letter(word, tulpe_letter)
      print_pendu()
      victory_of_defeat()
          
       


# Parametre du jeu
def main() :
   # initialise le mot
   set_word_for_game()
   # Recupere les tentatives de l'utilisateur 
   game()
   


# # on lance le programme
main()

