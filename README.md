# GessGame

Bienvenue dans **GessGame**, une implémentation Python du jeu classique du pendu (également appelé "Hangman") ! Testez vos connaissances, votre vocabulaire, et amusez-vous à deviner les mots en tentant de ne pas vous faire "pendre". Ce projet est conçu pour être évolutif, avec des fonctionnalités supplémentaires prévues dans les prochaines versions.

---

## Fonctionnalités
- **Mot mystère aléatoire** : Un mot est sélectionné au hasard à partir d'une liste de mots prédéfinis (fichier `words.py`).
- **Interface texte simple** : Jouez directement dans le terminal.
- **Illustrations du pendu** : Les différents états du pendu sont affichés à l'écran (provenant du fichier `pendu.py`).
- **Gestion des tentatives** : Vous avez un nombre limité de tentatives (par défaut 6) pour deviner le mot avant de perdre.
- **Rejouer ou quitter** : Une fois la partie terminée, choisissez de rejouer ou de quitter.

---

## Installation

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/gessgame.git
   cd gessgame
   ```

2. **Assurez-vous d'avoir Python installé** : Ce projet nécessite Python 3.6 ou une version ultérieure. Pour vérifier votre version :
   ```bash
   python --version
   ```

3. **Exécutez le jeu** :
   ```bash
   python gessgame.py
   ```

---

## Structure du projet
- **gessgame.py** : Fichier principal qui contient la logique du jeu.
- **pendu.py** : Contient les différents dessins illustrant les étapes du pendu.
- **words.py** : Une liste de mots utilisés comme mots mystères.

---

## Utilisation

1. Lorsque vous lancez le programme, un mot mystère est choisi aléatoirement.
2. Entrez une lettre à chaque tour pour deviner le mot. Vous pouvez voir les lettres révélées et le nombre de tentatives restantes.
3. Si vous devinez toutes les lettres avant la fin des tentatives, vous gagnez ! Sinon, vous perdez et le mot mystère est révélé.
4. Une fois la partie terminée, vous pouvez choisir de rejouer ou de quitter.

---

## Fonctionnalités futures
Voici quelques évolutions prévues pour les prochaines versions :

1. **Niveaux de difficulté** :
   - Facile : mots courts et courants.
   - Moyen : mots plus longs et complexes.
   - Difficile : mots rares.

2. **Thèmes** :
   - Catégories comme animaux, pays, sciences, etc.

3. **Jokers** :
   - Indices pour aider le joueur (exemple : révéler une lettre ou indiquer la catégorie du mot).

---

## Contribution
Les contributions sont les bienvenues ! Voici comment vous pouvez aider :

1. **Signaler des bugs** : Utilisez l'onglet "Issues" du dépôt.
2. **Proposer des idées** : Soumettez vos suggestions d'améliorations ou de nouvelles fonctionnalités.
3. **Soumettre des modifications** : Créez une branche, faites vos modifications, et ouvrez une Pull Request :
   ```bash
   git checkout -b feature/nouvelle-fonctionnalite
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   git push origin feature/nouvelle-fonctionnalite
   ```

---

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

---

## Remerciements
Merci d'avoir essayé **GessGame** ! Vos retours sont précieux et nous aideront à améliorer le jeu. 

Amusez-vous bien et bon courage pour deviner les mots !

