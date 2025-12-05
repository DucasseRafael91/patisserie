import threading
import time
import math
from abc import ABC, abstractmethod


class Recipient:
    def __init__(self, nom, contenu=None):
        self.nom = nom
        self.contenu = contenu if contenu is not None else []


class Commis(threading.Thread, ABC):
    def __init__(self, nom, recipient: Recipient):
        super().__init__()
        self.nom = nom
        self.recipient = recipient

    @abstractmethod
    def run(self):
        pass


class Ingredient(threading.Thread, ABC):
    def __init__(self, nom, quantite, unite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite
        self.unite = unite


class Appareil:
    def __init__(self, nom):
        self.nom = nom
        self.ingredients = []

    def ajouter_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients


class BatteurOeufs(Commis):
    def __init__(self, nom, recipient, nb_oeufs):
        super().__init__(nom, recipient)
        self.nb_oeufs = nb_oeufs

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"[{self.nom}] Je bats les {self.nb_oeufs} œufs, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(Commis):
    def __init__(self, nom, quantite, recipient):
        super().__init__(nom, recipient)
        self.quantite = quantite

    def run(self):
        print(f"[{self.nom}] Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(2)
        print(f"[{self.nom}] Je verse l'eau dans une casserole")
        time.sleep(1)
        print(f"[{self.nom}] J'y pose le bol rempli de chocolat")
        time.sleep(1)

        nb_tours = math.ceil(self.quantite / 10)

        for no_tour in range(1, nb_tours + 1):
            print(f"[{self.nom}] Je mélange {self.quantite} g de chocolat, tour n°{no_tour}")
            time.sleep(0.8)


class Oeuf(Ingredient):
    pass


class Chocolat(Ingredient):
    pass


if __name__ == "__main__":
    # Création des récipients
    casserolle_fer = Recipient("Casserolle en fer", [])
    casserolle_inox = Recipient("Casserolle en inox", [])
    bol = Recipient("Bol en Inox", [])

    # Commis
    batteur = BatteurOeufs("Jean", bol, 6)
    fondeurA = FondeurChocolat("Marie", 200, casserolle_fer)
    fondeurB = FondeurChocolat("Pierre", 100, casserolle_inox)

    # Lancement
    batteur.start()
    fondeurA.start()
    fondeurB.start()

    batteur.join()
    fondeurA.join()
    fondeurB.join()

    print("\nJe peux à présent incorporer le chocolat aux œufs")
