class croiseur(object):

    def __init__(self, num_serie, modele='destroyer'):
        self.modele = "Tector"
        self.num_serie = num_serie
        self.__modele = modele

    def __repr__(self):
        # todo: dessiner un croiseur avec les places occupées en asciiart
        return f"""modele: {self.modele}"""

    def depart(self):
        # vérifier si pilote
        # faire partir le croiseur
        pass


if __name__ == "__main__":
    mon_croiseur = croiseur('Executor', 'Interstellaire')
    print(mon_croiseur)
