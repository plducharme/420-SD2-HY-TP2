import unittest
from livre import Occurences, Statistiques, Livre


class TestOccurrences(unittest.TestCase):

    def setUp(self):
        self.occurences = Occurences(caractere="a", occurences=10)

    def test_caratere(self):
        self.assertEqual(self.occurences.caractere, "a")
        self.occurences.caractere = "b"
        self.assertEqual(self.occurences.caractere, "b")

    def test_occurrences(self):
        self.assertEqual(self.occurences.occurences, 10)
        self.occurences.occurences = 20
        self.assertEqual(self.occurences.occurences, 20)

    def test_lt(self):
        occurences2 = Occurences(caractere="e", occurences=50)
        self.assertLess(self.occurences, occurences2)


class TestStatistiques(unittest.TestCase):

    def setUp(self):
        self.occurrences = [Occurences(chr(x), x) for x in range(0, 255)]
        self.stats = Statistiques(nb_de_mots=1337, liste_occurences=self.occurrences)

    def test_nb_mots(self):
        self.assertEqual(self.stats.nb_de_mots, 1337)
        self.stats.nb_de_mots = 555
        self.assertEqual(self.stats.nb_de_mots, 555)

    def test_occurences(self):
        self.assertEqual(self.stats.liste_occurences, self.occurrences)
        occurrences2 = [Occurences(chr(x-1), x) for x in range(1, 256)]
        self.stats.liste_occurences = occurrences2
        self.assertEqual(self.stats.liste_occurences, occurrences2)


class TestLivre(unittest.TestCase):

    def setUp(self):
        self.livre = Livre(titre="Malphas 1: Le cas des casiers carnassiers", texte="test exemple",
                           auteur="Patrick Sénécal")

    def test_titre(self):
        self.assertEqual(self.livre.titre, "Malphas 1: Le cas des casiers carnassiers")
        self.livre.titre = "Malphas 2: Torture, luxure et lecture"
        self.assertEqual(self.livre.titre, "Malphas 2: Torture, luxure et lecture")

    def test_texte(self):
        self.assertEqual(self.livre.texte, "test exemple")
        self.livre.texte = "nouveau texte"
        self.assertEqual(self.livre.texte, "nouveau texte")

    def test_statistiques(self):
        occurrences = [Occurences(chr(x), x) for x in range(0, 255)]
        stats = Statistiques(nb_de_mots=1337, liste_occurences=occurrences)
        self.livre.statistiques = stats
        self.assertEqual(self.livre.statistiques, stats)
