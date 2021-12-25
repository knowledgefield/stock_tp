from database import *
from database.stock import StockDataBase

if __name__ == "__main__":
    print("Bienvenu dans le programme de gestion de stock:")
    print("***********************************************")

    stock_global = StockDataBase()
    while True:
        print("Enter un chiffre représentant votre choix:")
        print("-----------------------------------------------")
        print("1: Ajouter un Article.")
        print("2: Afficher tous Article.")
        print("3: Supprimmer un Article.")
        print("4: Rechercher Article(s).")
        print("5: Modifier un Article.")
        print("6: Quitter.")
        print("-----------------------------------------------")

        try:
            choix_utilisateur = int(input("Quel est votre choix: "))
            if choix_utilisateur == 6:
                print()
                print("Merci d'avoire uliliser notre programme.")
                print("Au Revoir!")
                print("----------------------------")
                break
            elif choix_utilisateur == 1:
                print("")
                print("-----------------------------------------------")
                nom = input("Le nom de l'article: ")
                quantite = int(input("La quantité: "))
                stock_global.ajouter_article(nom, quantite)
                print("Votre article à était ajouter.")
                print("")
                print("-----------------------------------------------")
            elif choix_utilisateur == 2:
                all_articles = stock_global.afficher_article()
                print("")
                print("-----------------------------------------------")
                for i in all_articles:
                    print(f"Code : {i[0]}  |  {i[1]} : {i[2]}")
                print("")
                print("-----------------------------------------------")
            elif choix_utilisateur == 3:
                print("")
                print("-----------------------------------------------")
                code_id = int(
                    input("Entrer le code de l'article a supprimer... "))
                all_articles = stock_global.afficher_article()
                success = False

                for i in all_articles:
                    if i[0] == code_id:
                        stock_global.supprimmer_article(code_id)
                        # afficher msg de confirmation
                        print()
                        print("-----------------------------------")
                        print(f"L'article {i[1]} à était supprimer.")
                        print("-----------------------------------")
                        print()
                        success = True

                if not success:
                    print()
                    print("-----------------------------------")
                    print("ERROR: Code Non Existant.")
                    print("-----------------------------------")
                    print()

            elif choix_utilisateur == 4:
                min_liste_article = []
                is_article_exist = False

                print("")
                print("-----------------------------------------------")
                articles_user = input(
                    "Entrer le nom de l'article à rechrecher (Séparer les article par une vergule) ... ")

                min_liste_article = articles_user.split(',')
                all_articles = stock_global.afficher_article()

                for i in min_liste_article:
                    for j in all_articles:
                        if i == j[1]:
                            print(f"{j[1]} : {j[2]}")
                            is_article_exist = True

                if not is_article_exist:
                    print("Aucun article de ce nom est trouvable.")

                print("")
                print("-----------------------------------------------")

            elif choix_utilisateur == 5:
                print("")
                print("-----------------------------------------------")

                code_modification = int(
                    input("Entrer le code de l'article a modifier... "))
                all_articles = stock_global.afficher_article()
                success_m = False

                for i in all_articles:
                    if i[0] == code_modification:
                        nom_article = input("Entrer le Nom de l'article: ")
                        qnt_article = int(input("Entrer la quantité: "))

                        stock_global.update_article(
                            code_modification, nom_article, qnt_article)
                        # afficher msg de confirmation
                        print()
                        print("-----------------------------------")
                        print(f"L'article {i[1]} à était Modifier.")
                        print("-----------------------------------")
                        print()
                        success_m = True

                if not success_m:
                    print()
                    print("-----------------------------------")
                    print("ERROR: Code Non Existant.")
                    print("-----------------------------------")
                    print()

                print("")
                print("-----------------------------------------------")

        except Exception as e:
            print()
            print("-----------------------------------")
            print("ERROR: S.V.P, Enter un choix valid.")
            print("-----------------------------------")
            print()
