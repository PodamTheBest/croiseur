from pack_personnes.personne import Personne


class PersonneStormtrooper(Personne):

    def __init__(self, stormtrooper):  # matricule, classe, num_siege):
        super().__init__(stormtrooper[0], stormtrooper[1])
        self.num_siege = stormtrooper[2]

    def __repr__(self):
        data = f"Matricule stormtrooper = {self.matricule}"
        return data

