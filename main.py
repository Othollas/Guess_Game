import math
import random 
from words import words as w
print(math.ceil(random.random()*10))

print(""" 
==========================================
!                                        !     
!            Le jeux du pendu            !
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
def get_word_for_game() :
    word = get_word()
    word = word.lower()
    defragmented_word = [(letter, False) for letter in word]
    defragmented_word = set(defragmented_word)
    return defragmented_word
# Initialiser le mot avec des _ si la lettre est à false

# Faire une entrer utilisateur 

# Comparer le choix utilisateur avec les lettres dans la liste de tulpe, si la lettre est dans dans la liste, elle passe à True et devient visible dans le mot à la place du _ 

# L'utilisateur auras 6 essais et à chaque essais rater le pendu sera construit

# si l'utilsateur à deviner le mot avant la fin de la construction du pendu alors il 

print(get_word_for_game())