import unittest
import re

from livre import Occurences, Statistiques, Livre
from analyseurlivre import Analyseur, DataUtils
from typing import List


class TestAnalyseurLivre(unittest.TestCase):

    def setUp(self):
        livre_nelligan = DataUtils.charger_livre(DataUtils.LE_VAISSEAU_D_OR)
        self.analyseur = Analyseur(livre_nelligan)

    def test_nb_mots(self):
        self.analyseur.analyser()
        min_mots = len(self.analyseur.livre.texte.split(" "))
        max_mots = len(re.sub("[^a-zA-ZÀ-ÿ \t\n\r\f\v]", " ", self.analyseur.livre.texte).split(" "))
        # Teste le nombre de mots
        self.assertIn(self.analyseur.livre.statistiques.nb_de_mots, range(min_mots, max_mots+1))

    def test_tri(self):
        self.analyseur.analyser()
        liste_occurences: List[Occurences] = [Occurences(chr(x), self.analyseur.livre.texte.count(chr(x))) for x in range(0, 256)]
        liste_occurences.sort()
        liste_occurences_analyseur: List[Occurences] = self.analyseur.livre.statistiques.liste_occurences
        i = 0
        for o in liste_occurences_analyseur:
            if o.occurences != liste_occurences[i].occurences:
                raise AssertionError("Nombre d'occurences différent")
            i += 1




