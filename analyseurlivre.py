from livre import Livre, Occurences, Statistiques


#######################################
# Auteur: nom1 (Github username)
# Auteur: nom2 (Github username)
# Auteur: nom3 (Github username)
#######################################
class DataUtils:

    ALICE_AU_PAYS_DES_MERVEILLES = 1
    LES_TROIS_MOUSQUETAIRES = 2
    LE_VAISSEAU_D_OR = 3

    @staticmethod
    def charger_livre(livre_id: int) -> Livre:

        match livre_id:

            case DataUtils.ALICE_AU_PAYS_DES_MERVEILLES:
                texte = DataUtils.__charger_texte_livre("./livres/aliceaupaysdesmerveilles.txt")
                livre = Livre("Alice aux pays des merveilles", texte, "Lewis Carroll")
                return livre
            case DataUtils.LES_TROIS_MOUSQUETAIRES:
                texte = DataUtils.__charger_texte_livre("./livres/lestroismousquetaires.txt")
                livre = Livre("Les trois mousquetaires", texte, "Alexandre Dumas")
                return livre
            case DataUtils.LE_VAISSEAU_D_OR:
                texte = DataUtils.__charger_texte_livre("./livres/levaisseaudor.txt")
                livre = Livre("Le vaisseau d'or", texte, "Émile Nelligan")
                return livre
            case _:
                raise ValueError("Mauvais id de livre! Utilisez une variable de classe")

    @staticmethod
    def __charger_texte_livre(fichier) -> str:
        texte = ""
        with open(fichier, "r", encoding="utf-8") as fichier_livre:
            for ligne in fichier_livre:
                texte += ligne
        return texte


class Analyseur:

    def __init__(self, livre: Livre):
        self.__livre = livre

    @property
    def livre(self) -> Livre:
        return self.__livre

    @livre.setter
    def livre(self, livre: Livre):
        self.__livre = livre

    # Compléter l'implémentation de la classe
    def analyser(self):
        # À implémenter
        pass


    @staticmethod
    def tri_peigne(liste):
        # À implémenter
        pass


if __name__ == '__main__':

    ### Scénarios de test
    print("\n########## Vaisseau d'or ###############")
    livre_nelligan = DataUtils.charger_livre(DataUtils.LE_VAISSEAU_D_OR)
    analyseur_nelligan = Analyseur(livre_nelligan)
    analyseur_nelligan.analyser()
    print(analyseur_nelligan.livre.statistiques.liste_occurences)
    print(analyseur_nelligan.livre.statistiques.nb_de_mots)

    print("\n########## Alice au pays des merveilles ###############")
    livre_carroll = DataUtils.charger_livre(DataUtils.ALICE_AU_PAYS_DES_MERVEILLES)
    analyseur_carroll = Analyseur(livre_carroll)
    analyseur_carroll.analyser()
    print(analyseur_carroll.livre.statistiques.liste_occurences)
    print(analyseur_carroll.livre.statistiques.nb_de_mots)

    print("\n########## Les trois mousquetaires ###############")
    livre_dumas = DataUtils.charger_livre(DataUtils.LES_TROIS_MOUSQUETAIRES)
    analyseur_dumas = Analyseur(livre_dumas)
    analyseur_dumas.analyser()
    print(analyseur_dumas.livre.statistiques.liste_occurences)
    print(analyseur_dumas.livre.statistiques.nb_de_mots)