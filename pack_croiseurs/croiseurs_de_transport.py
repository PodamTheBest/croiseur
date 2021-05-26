from pack_croiseurs.croiseur import croiseur
from pack_personnes.personne_stormtrooper import PersonneStormtrooper
from pack_personnes.personne_pilote import PersonnePilote


class croiseurDeTransport(croiseur):

    def __init__(self, num_serie, modele='destroyer'):
        super().__init__(num_serie, modele=modele)
        self.__pilote = None
        self.__liste_stormtroopers = list()

    def __anonymiser_liste(self):
        liste_temp = list()
        for stormtrooper in self.__liste_stormtroopers:
            liste_temp.append(stormtrooper)
        return liste_temp

    def get_liste_stormtroopers(self):
        liste_simplifiee = self.__anonymiser_liste()
        return liste_simplifiee

    def embarquer_pilote(self, pilote_candidat):
        pilote_accepte = False
        if isinstance(pilote_candidat, PersonnePilote):
            self.__pilote = pilote_candidat
            pilote_accepte = True
        return pilote_accepte

    def embarquer_stormtrooper(self, stormtrooper_candidat):
        stormtrooper_accepte = False
        if isinstance(stormtrooper_candidat, PersonneStormtrooper):
            self.__liste_stormtroopers.append(stormtrooper_candidat)
            stormtrooper_accepte = True
        return stormtrooper_accepte

    def depart(self):
        if self.__pilote is not None:
            return "Piou Piou on va faire la guerre"
