'''Phase 1 du projet: analyseur de commande et chercheur d'historique'''


import argparse, json, requests, datetime
from datetime import datetime as dt


def analyser_commande():
    """
    Générer un interpréteur de commande.

    Returns:
        Un objet Namespace tel que retourné par parser.parse_args().
        Cet objet aura l'attribut «symboles» représentant la liste des
        symboles à traiter, et les attributs «début», «fin» et «valeur»
        associés aux arguments optionnels de la ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description = 'Va chercher les valeurs historiques de symboles boursiers')
    parser.add_argument('symbole', nargs='+', help = "Nom d'un symbole boursier")
    parser.add_argument('-f', '--fin', dest = 'fin', metavar='DATE',
        default = dt.today().date().strftime("%Y-%m-%d",
        help = 'La date recherchée la plus ancienne (format: AAAA-MM-JJ)'))
    parser.add_argument('-d', '--début', dest = 'début', metavar= 'DATE',
        help = 'La date recherchée la plus récente (format: AAAA-MM-JJ)')
    parser.add_argument('-v', '--valeur',
        help = "La valeur désirée (par défaut: fermeture)", default= 'fermeture',
        choices=['fermeture', 'ouverture', 'min', 'max', 'volume'])


    return parser.parse_args()


def produire_historique():
    '''Produit un historique en fonction du symbole et de la date demandé'''

    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    timeline = {"début":date_debut, "fin": date_fin}
    reponse = json.loads(requests.get(url, timeline).text)
    historique = []
    for keys in reponse["historique"]:
        historique.append((dt.strptime(keys, "%Y-%m-%d").date() ,
                            reponse["historique"][keys][info_demande]))

    return historique