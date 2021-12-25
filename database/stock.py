import sqlite3


class StockDataBase:
    nom_article = ""
    quantite = 0
    code = ""

    def __init__(self):
        self.init_database()

    def init_database(self):
        with sqlite3.connect("data/stock.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS stock (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nom_article TEXT NOT NULL,
                                quantite INTEGER NOT NULL)
            """)
            connection.commit()

    def ajouter_article(self, nom, qnt):
        with sqlite3.connect("data/stock.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO stock (nom_article, quantite) VALUES (?, ?)""",
                           (nom, qnt))

    def afficher_article(self):
        with sqlite3.connect("data/stock.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM stock""")
            donnee = cursor.fetchall()

        return donnee

    def supprimmer_article(self, id_article):
        with sqlite3.connect("data/stock.db") as connection:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM stock WHERE id = ?""", (id_article,))
            connection.commit()

    def update_article(self, id_a, nom, qnt):
        with sqlite3.connect("data/stock.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                """UPDATE stock SET nom_article=?, quantite=? WHERE id=?""", (nom, qnt, id_a))
            connection.commit()
