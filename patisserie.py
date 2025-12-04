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

class BatteurOeufs(Commis):
    def __init__(self, nom, nb_oeufs):
        super().__init__(nom)
        self.nb_oeufs = nb_oeufs

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"[{self.nom}] Je bats les {self.nb_oeufs} œufs, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(Commis):
    def __init__(self, nom, quantite):
        super().__init__(nom)
        self.quantite = quantite  # en grammes

    class Oeuf(Ingredient):
        def __init__(self, nom, quantite, unite):
            super().__init__(nom, quantite, unite)

    class Chocolat(Ingredient):
        def __init__(self, nom, quantite, unite):
            super().__init__(nom, quantite, unite)

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


if __name__ == "__main__":
    batteur = BatteurOeufs("Jean", 6)
    fondeur = FondeurChocolat("Marie", 200)

    batteur.start()
    fondeur.start()

    batteur.join()
    fondeur.join()

    print("\nJe peux à présent incorporer le chocolat aux œufs")
