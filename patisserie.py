import threading
import time
import math
from abc import ABC, abstractmethod


class Commis(threading.Thread, ABC):
    def __init__(self, nom):
        threading.Thread.__init__(self)
        self.nom = nom

    @abstractmethod
    def run(self):
        pass


class Ingredient(threading.Thread, ABC):
    def __init__(self, nom, quantite, unite):
        threading.Thread.__init__(self)
        self.nom = nom
        self.quantite = quantite
        self.unite = unite


class Appareil:
    """
    Un appareil représente un mélange homogène d'ingrédients
    avant cuisson ou turbinage.
    """

    def __init__(self, nom):
        self.nom = nom
        self.ingredients = []

    def ajouter_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients[:]


class BatteurOeufs(Commis):
    def __init__(self, nom, nb_oeufs):
        super().__init__(nom)
        self.nb_oeufs = nb_oeufs
        self.appareil = appareil

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"[{self.nom}] Je bats les {self.nb_oeufs} œufs, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(Commis):
    class Oeuf(Ingredient):
        def __init__(self, quantite):
            super().__init__("Œuf", quantite, "pièces")

    class Chocolat(Ingredient):
        def __init__(self, quantite):
            super().__init__("Chocolat", quantite, "g")

    def __init__(self, nom, quantite, appareil=None):
        super().__init__(nom)
        self.quantite = quantite
        self.appareil = appareil

    def run(self):
        print(f"[{self.nom}] Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print(f"[{self.nom}] Je verse l'eau dans une casserole")
        time.sleep(2)
        print(f"[{self.nom}] J'y pose le bol rempli de chocolat")
        time.sleep(1)

        nb_tours = math.ceil(self.quantite / 10)

        for no_tour in range(1, nb_tours + 1):
            print(f"[{self.nom}] Je mélange {self.quantite} g de chocolat, tour n°{no_tour}")
            time.sleep(1)


class Oeuf(Ingredient):
    def __init__(self, nom, quantite, unite):
        super().__init__(nom, quantite, unite)


class Chocolat(Ingredient):
    def __init__(self, nom, quantite, unite):
        super().__init__(nom, quantite, unite)


if __name__ == "__main__":
    # Création d'un appareil
    appareil = Appareil("Appareil chocolat-œufs")

    # Commis
    batteur = BatteurOeufs("Jean", 6)
    fondeur = FondeurChocolat("Marie", 200)

    # Lancement
    batteur.start()
    fondeur.start()

    batteur.join()
    fondeur.join()

    print("\nJe peux à présent incorporer le chocolat aux œufs")

    #oeuf = Oeuf("Oeufs fermiers", 6, "pièces")
    #chocolat = Chocolat("Chocolat noir", 200, "g")
    #appareil.ajouter_ingredient(oeuf)
    #appareil.ajouter_ingredient(chocolat)
    #for ingredient in appareil.get_ingredients():
    #   print(f"- {ingredient.quantite} {ingredient.unite} de {ingredient.nom}")
