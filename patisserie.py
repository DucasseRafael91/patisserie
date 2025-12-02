import threading
import time
import math
from abc import ABC


class Commis(threading.Thread, ABC):
    def __init__(self, nom, recipient):
        threading.Thread.__init__(self)
        self.nom = nom
        self.recipient = recipient

    def dire(self, message):
        print(f"[{self.nom} - {self.recipient.nom}] {message}")


class BatteurOeufs(Commis):
    def __init__(self, nom, nb_oeufs, recipient):
        super().__init__(nom, recipient)
        self.nb_oeufs = nb_oeufs

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            self.dire(f"Je bats les {self.nb_oeufs} {self.recipient.contenu.nom}, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(Commis):
    def __init__(self, nom, quantite, recipient):
        super().__init__(nom, recipient)
        self.quantite = quantite  # en grammes

    def run(self):
        self.dire("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        self.dire("Je verse l'eau dans une casserole")
        time.sleep(2)
        self.dire(f"J'y pose le {self.recipient.nom} rempli de {self.recipient.contenu.nom}")
        time.sleep(1)

        nb_tours = math.ceil(self.quantite / 10)

        for no_tour in range(1, nb_tours + 1):
            self.dire(f"Je mélange {self.quantite} {self.recipient.contenu.unite} de {self.recipient.contenu.nom} "
                      f"tour n°{no_tour}")
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
        print(f"\nJe mélange  '{self.nom}' pour obtenir une préparation homogène…")
        time.sleep(2)
        print(f"L'appareil '{self.nom}' est prêt.\n")


class Recipient:
    def __init__(self, nom, contenu):
        self.nom = nom
        self.contenu = contenu

    def ajouter(self, contenu):
        self.contenu = contenu


if __name__ == "__main__":

    oeufs = Oeuf("oeuf fermier", 6, "unités")
    chocolat = Chocolat("chocolat patissier", 200, "g")

    recipient_batteur = Recipient("Casserole", oeufs)
    recipient_fondeur = Recipient("Bol en Inox A", chocolat)

    batteur = BatteurOeufs("Pierre", 6, recipient_batteur)
    fondeur = FondeurChocolat("Marie", 200, recipient_fondeur)

    batteur.start()
    fondeur.start()

    batteur.join()
    fondeur.join()

    print("\nJe peux à présent incorporer le chocolat aux oeufs")

    appareil = Appareil("Base Gateau au chocolat ")
    appareil.ajouter(oeufs)
    appareil.ajouter(chocolat)
    appareil.melanger()
