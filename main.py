import math
import random 
from words import words as w

word = ""
defragmented_word = []
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
    global defragmented_word
    word = get_word().lower()
    defragmented_word = [(letter, False) for letter in word]
    defragmented_word = set(defragmented_word)
    hide_letter(word, defragmented_word)
    return None


    



# Initialiser le mot avec des _ si la lettre est à false

def hide_letter(word, defragmented_word) : 
  global blank_word
  global print_blank_word
 
  for letter in word :
     for tulpe in defragmented_word :
        if letter in tulpe[0] and tulpe[1] == False :
           letter = '_'
           blank_word.append(letter)
           print_blank_word += letter
 
def show_letter() :
  # ici je dois verifier si les tulpes sont True ou False et montrer la lettre correspondante.
   return None


# Fonction pour comparer l'entré avec
def compare_letter(user_letter):
   global defragmented_word
   defragmented_word_find = [tulpe for tulpe in defragmented_word if tulpe[0] == user_letter and tulpe[1] != True]
   if len(defragmented_word_find) > 0 and defragmented_word_find[0][1] != True:
      print(f"avant modification{defragmented_word_find[0][1]}")
      defragmented_word.remove((user_letter, False))
      new_entrie = (user_letter, True)
      defragmented_word.add(new_entrie)
      

   elif len(defragmented_word_find) > 0 and defragmented_word_find[0][1] == True: 
      print("Vous avez deja cette lettre")

   else:
     print("Cette lettre n'existe pas")
   print(f"aprés modification{defragmented_word}")
   


# Faire une entrer utilisateur 
def get_letter_from_user() :
   i=6
   while i >= 0 :
    print(print_blank_word)
    user_letter = input("Entrez une lettre. ").lower()
    if len(user_letter) > 1 :
       print(f"Non vous devez entrez qu'une seule lettre : tentative restante {i}")
    elif user_letter.isdigit(): 
       print(f"Non vous devez entrez qu'une seule lettre : tentative restante {i}")
    else :
       compare_letter(user_letter)
       print("jusque là c'est ok")
       
       # Fonction qui compare 
       
       
          
       
# Comparer le choix utilisateur avec les lettres dans la liste de tulpe, si la lettre est dans dans la liste, elle passe à True et devient visible dans le mot à la place du _ 

# L'utilisateur auras 6 essais et à chaque essais rater le pendu sera construit

# si l'utilsateur à deviner le mot avant la fin de la construction du pendu alors il 


# Parametre du jeu
def main() :
   # initialise le mot
   set_word_for_game()
   # Recupere les tentatives de l'utilisateur 
   get_letter_from_user()


# on lance le programme
main()