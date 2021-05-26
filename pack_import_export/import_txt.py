import csv


class ImportTxt:

    def __init__(self, matricule_fichier_txt):
        self.__liste_stormtroopers = list()
        # todo: verifier existance fichier
        self.__lire_fichier(matricule_fichier_txt)

    def __lire_fichier(self, matricule_fichier_txt):
        with open(matricule_fichier_txt) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for data in reader:
                if len(data) == 3:
                    matricule, classe, siege = data[0].capitalize(), data[1].capitalize(), data[2]
                    self.__liste_stormtroopers.append( (classe, matricule, siege) )

    def get_liste_stormtroopers(self):
        """
        return liste troupes
        """
        return self.__liste_stormtroopers


if __name__ == '__main__':
    from pprint import pprint
    importer = ImportTxt('../liste_stormtroopers.txt')
    pprint(importer.get_liste_stormtroopers())
