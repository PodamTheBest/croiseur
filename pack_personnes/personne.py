class Personne(object):

    def __init__(self, matricule, classe):
        self.classe = classe
        self.matricule = matricule

    def __repr__(self):
        return f"""matricule: {self.matricule}\nclasse: {self.classe}"""


if __name__ == "__main__":
    ma_personne = Personne('Phasma', 'Captain')
    print(ma_personne)
