from pack_croiseurs.croiseur import croiseur
from pack_croiseurs.croiseurs_de_transport import croiseurDeTransport
from pack_personnes.personne import Personne
from pack_personnes.personne_pilote import PersonnePilote
from pack_personnes.personne_stormtrooper import PersonneStormtrooper
from pack_import_export.import_txt import ImportTxt
from pprint import pprint

# Il me faut un croiseur
mon_croiseur = croiseurDeTransport('Executor', 'Interstellaire')
print(mon_croiseur)

# Affecter un pilote
mon_pilote = PersonnePilote('FN-4521', 'Pilote', 33, 'pilote')
print(mon_pilote)

if mon_croiseur.embarquer_pilote(mon_pilote):
    print("Le pilote est dans le croiseur")

    # Enregistrer des stormtroopers

    importer = ImportTxt('liste_stormtroopers.txt')
    liste_stormtroopers_en_attente = importer.get_liste_stormtroopers()

    for stormtrooper_en_attente in liste_stormtroopers_en_attente:
        mon_stormtrooper = PersonneStormtrooper(stormtrooper_en_attente)
        if mon_croiseur.embarquer_stormtrooper(mon_stormtrooper):
            print(f"{mon_stormtrooper.matricule} est dans le croiseur !!")

    # Partir en guerre
    chaine_depart = mon_croiseur.depart()
    print(chaine_depart)

