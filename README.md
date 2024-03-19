# Travail Pratique 2 - Analyseur de livres
Vous devez implémenter un analyseur de livres simple. L'analyseur va prendre le texte d'un livre et doit retourner des
statistiques sur ce livre.

## Prérequis
- Interpréteur Python >= 3.10

## Requis
- Dans le module *livre.py*, implémenter les classes suivantes:
    ### classe Occurrences
    - Va contenir le nombre d'occurences dans le texte d'un certain caractère.
    - doit contenir deux variables d'instance
      - caractere: str, le caractère
      - occurences: int, le nombre de fois qu'il apparait dans le texte
    - Doit respecter l'encapsulation (utiliser le décorateur @property)
    - Doit implémenter les opérateurs de comparaisons pour que la comparaison entre deux objets Occurences puissent être
comparés directement. La comparaison se fera en utilisant la variable *occurences*.
    > occurence1 < occurence2
    
    au lieu de:
    > occurence1.occurences < occurence2.occurences

    - Écrire la Docstrings de classe
    
    ### classe Statistiques
    - Va contenir les statistiques du livre
    - doit contenir deux variables d'instance
      - nb_de_mots: int, le nombre de mots dans le livre (voir plus bas pour les règles)
      - liste_occurences: List[Occurences]
    - Doit respecter l'encapsulation (utiliser le décorateur @property)
    - Écrire la Docstrings de classe

    ### classe Livre
    - Va contenir l'information du livre
    - doit contenir les variables d'instance
      - titre: str, le titre du livre
      - texte: str, le texte du livre
      - auteur: str, l'auteur du livre
      - statistiques: Statistiques, un objet Statistiques
    - Doit définir un constructeur:
        ```
       def __init__(self, titre: str, texte: str, auteur: str):
      ```
    - Doit respecter l'encapsulation (utiliser le décorateur @property)
    - Écrire la Docstrings de classe
  
- Dans le module *analyseurlivre.py*:
    - Ne pas toucher à la classe DataUtils et aux scénarios de tests
    - DataUtils permet de créer les objets Livre en lisant le texte des livres à partir d'un fichier texte. Ne pas modifier.
    - Vous devez implémenter la méthode *analyser(self)* de la classe *Analyseur*
      - Cette méthode doit créer un objet Statistiques contenant le nombre de mots et une liste d'Occurences
        - Le nombre de mots est le nombre de mots du texte
          - Les mots composés avec un tiret (-) ou une barre oblique (/) compte pour un mot
          - Faire attention aux mots contenant des caractères spéciaux au début (*leading*) et à la fin (*trailing*)
          > ex: [Illustration] (De la part de Mlle Alice.)_
        - La liste d'Occurences contient des objets Occurences
          - Un objet Occurences contient un caractère et son nombre d'occurences
          - Le texte est décodé en [UTF-8](https://fr.wikipedia.org/wiki/UTF-8)
            - Ceci veut dire que les caractères sont encodés sur 8-bit
              - Il y a donc 256 (2^8) caractères possibles (0-255)
              - Votre liste devrait être d'une longueur de 256 éléments
      - Une fois la liste d'occurences générée, vous devez appeler la méthode *tri_peigne(liste)* pour trier la liste d'occurences.
        - Voir la définition du tri à peigne dans la prochaine section
      
    
## Le tri à peigne
[Le tri à peigne](https://fr.wikipedia.org/wiki/Tri_%C3%A0_peigne) est une modification du tri à bulle ascendant. Le tri à bulle
est souvent peu performant car les petites valeurs prennent du temps à être ramené vers le début (tortues). Ceci est dû
entre autre par le fait que les comparaisons sont fait entre voisins (intervalle de 1). Le tri à peigne modifie ceci pour 
introduire un intervalle qui est réduit à chaque passe. On va utiliser la variante "comb-11" qui change l'intervalle dans certains
cas pour améliorer la performance. Voici un pseudo-code:

```
        triée := False
        # Au début, on assigne l'intervalle au maximum possible
        intervalle := longueur de la liste
        # Facteur par lequel on réduit l'intervalle à chaque passe
        facteur_de_reduction := 1.3

        Tant que non triée
            intervalle := plancher de la division de intervalle / facteur_de_reduction
            # Si l'intervalle est plus petit ou égal à 1, on l'assigne à un (comparaison avec le voisin vers la fin)
            si intervalle <= 1
                intervalle = 1
                triée = True
            # Variante comb-11, si l'intervalle est 9 ou 10, on l'assigne à 11 
            ou si intervalle = 9 or intervalle = 10:
                intervalle = 1

            # On fait comme un tri à bulle mais avec un intervalle de comparaison au lieu 
            i := 0
            Tant que i + intervalle < longueur de la liste:
                si liste[i] > liste[i+intervalle]
                    échanger(liste[i] et liste[i+intervalle])
                    # On a fait un échange cette passe si, on ne peut garantir que la liste est triée
                    triée = False
                i += 1


```
        
## Évaluation
La remise se fait par Github classroom. Vous devez faire vos "push" avant la date limite de remise. Après cette date, Github
refuse les "push". Ce travail pratique compte pour 15% de la note finale.

- Ne pas oublier de mettre vos noms et utilisateurs Github
- Des points seront enlevés pour le non-respect des PEPs.
- classes dans livres.py (5 pts)
- la méthode analyser(self) dans la classe Analyseur (5 pts)
- la méthode tri_peigne(liste) dans la classe Analyseur (5 pts)
    