from pack_personnes.personne import Personne


class PersonnePilote(Personne):

    def __init__(self, matricule, classe, Exp, Statut):
        super().__init__(matricule, classe)
        self.exp = Exp
        self.status = Statut

    def conduire(self):
        # print("héééé zé parti")
        pass

    def __repr__(self):
        data = f"matricule pilote = {self.matricule}"
        return data
