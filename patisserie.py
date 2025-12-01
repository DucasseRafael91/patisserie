import threading
import time
import math
from abc import ABC, abstractmethod


class Commis(threading.Thread, ABC):
    def __init__(self, nom):
        threading.Thread.__init__(self)
        self.nom = nom

    def say(self, message):
        print(f"[{self.nom}] {message}")


class BatteurOeufs(Commis):
    def __init__(self, nom, nb_oeufs):
        super().__init__(nom)
        self.nb_oeufs = nb_oeufs

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            self.say(f"Je bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(Commis):
    def __init__(self, nom, quantite):
        super().__init__(nom)
        self.quantite = quantite  # en grammes

    def run(self):
        self.say("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        self.say("Je verse l'eau dans une casserole")
        time.sleep(2)
        self.say("J'y pose le bol rempli de chocolat")
        time.sleep(1)

        nb_tours = math.ceil(self.quantite / 10)

        for no_tour in range(1, nb_tours + 1):
            self.say(f"Je mélange {self.quantite} g de chocolat, tour n°{no_tour}")
            time.sleep(1)


if __name__ == "__main__":
    batteur = BatteurOeufs("Pierre", 6)
    fondeur = FondeurChocolat("Marie", 200)

    batteur.start()
    fondeur.start()

    batteur.join()
    fondeur.join()

    print("\nJe peux à présent incorporer le chocolat aux oeufs")
