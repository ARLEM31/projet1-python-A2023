'''Ce programme sert à faire runner la phase 1 du projet'''


from datetime import datetime as dt
from phase1 import analyser_commande, produire_historique

if __name__ == "__main__":
    args = analyser_commande()
    for symbole in args.symbole:
        if args.début is None:
            date = dt.strptime(args.fin, "%Y-%m-%d").date()

            print(f'titre={symbole}: valeur={args.valeur}, début={date}, fin={date}')
            print(produire_historique(symbole, args.fin, args.fin, args.valeur))

        else:
            début = dt.strptime(args.début, "%Y-%m-%d").date()
            fin = dt.strptime(args.fin, "%Y-%m-%d").date()

            print(f'titre={symbole}: valeur={args.valeur}, début={début}, fin={fin}')
            print(produire_historique(symbole, args.début, args.fin, args.valeur))
