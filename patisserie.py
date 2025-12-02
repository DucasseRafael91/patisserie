import threading
import time
import math
from abc import ABC


class Commis(threading.Thread, ABC):
    def __init__(self, nom):
        threading.Thread.__init__(self)
        self.nom = nom

    def dire(self, message):
        print(f"[{self.nom}] {message}")


class BatteurOeufs(Commis):
    def __init__(self, nom, nb_oeufs):
        super().__init__(nom)
        self.nb_oeufs = nb_oeufs

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            self.dire(f"Je bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(Commis):
    def __init__(self, nom, quantite):
        super().__init__(nom)
        self.quantite = quantite  # en grammes

    def run(self):
        self.dire("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        self.dire("Je verse l'eau dans une casserole")
        time.sleep(2)
        self.dire("J'y pose le bol rempli de chocolat")
        time.sleep(1)

        nb_tours = math.ceil(self.quantite / 10)

        for no_tour in range(1, nb_tours + 1):
            self.dire(f"Je mélange {self.quantite} g de chocolat, tour n°{no_tour}")
            time.sleep(1)


class Ingredient(threading.Thread, ABC):
    def __init__(self, nom, quantite, unite):
        threading.Thread.__init__(self)
        self.nom = nom
        self.quantite = quantite
        self.unite = unite


class Oeuf(Ingredient):
    def __init__(self, nom, quantite, unite):
        super().__init__(nom, quantite, unite)


class Chocolat(Ingredient):
    def __init__(self, nom, quantite, unite):
        super().__init__(nom, quantite, unite)


class Appareil:
    def __init__(self, nom):
        self.nom = nom
        self.ingredients = []

    def ajouter(self, ingredient):
        """Ajoute un ingrédient (objet Ingredient)."""
        self.ingredients.append(ingredient)

    def melanger(self):
        """Simule un mélange homogène."""
        print(f"\nJe mélange soigneusement l'appareil '{self.nom}' pour obtenir une préparation homogène…")
        time.sleep(2)
        print(f"L'appareil '{self.nom}' est prêt.\n")


if __name__ == "__main__":
    batteur = BatteurOeufs("Pierre", 6)
    fondeur = FondeurChocolat("Marie", 200)

    batteur.start()
    fondeur.start()

    batteur.join()
    fondeur.join()

    print("\nJe peux à présent incorporer le chocolat aux oeufs")

    # Création des ingrédients correspondants
    oeufs = Oeuf("œufs battus", 6, "unités")
    chocolat = Chocolat("chocolat fondu", 200, "g")

    appareil = Appareil("Base Gateau au chocolat ")
    appareil.ajouter(oeufs)
    appareil.ajouter(chocolat)
    appareil.melanger()

