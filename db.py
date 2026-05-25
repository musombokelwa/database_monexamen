import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='monexamen',
            user='root',
            password='1234'
        )
        return conn
    except Error as e:
        print(f"Erreur lors de la connexion : {e}")
        return None

# --- Fonctions pour ETUDIANT ---
def insert_etudiant(nom, prenom, email, promotion, departement, password):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO etudiant (nom, prenom, email, promotion, departement, password) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nom, prenom, email, promotion, departement, password))
            conn.commit()
            print("Etudiant inséré avec succès.")
        except Error as e:
            print(f"Erreur d'insertion (etudiant) : {e}")
        finally:
            cursor.close()
            conn.close()

def get_all_etudiants():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM etudiant")
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur de lecture (etudiant) : {e}")
            return []
        finally:
            cursor.close()
            conn.close()

# --- Fonctions pour LIVRE ---
def insert_livre(titre):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO livre (titre) VALUES (%s)"
            cursor.execute(query, (titre,))
            conn.commit()
            print("Livre inséré avec succès.")
        except Error as e:
            print(f"Erreur d'insertion (livre) : {e}")
        finally:
            cursor.close()
            conn.close()

def get_all_livres():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM livre")
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur de lecture (livre) : {e}")
            return []
        finally:
            cursor.close()
            conn.close()

# --- Fonctions pour INTERROGATION ---
def insert_interrogation(titre, promotion, departement):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO interrogation (titre, promotion, departement) VALUES (%s, %s, %s)"
            cursor.execute(query, (titre, promotion, departement))
            conn.commit()
            print("Interrogation insérée avec succès.")
        except Error as e:
            print(f"Erreur d'insertion (interrogation) : {e}")
        finally:
            cursor.close()
            conn.close()

def get_all_interrogations():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM interrogation")
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur de lecture (interrogation) : {e}")
            return []
        finally:
            cursor.close()
            conn.close()

# --- Fonctions pour EXAMEN ---
def insert_examen(titre, promotion, departement):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Supposons que la table examen ait une structure similaire à interrogation
            query = "INSERT INTO examen (titre, promotion, departement) VALUES (%s, %s, %s)"
            cursor.execute(query, (titre, promotion, departement))
            conn.commit()
            print("Examen inséré avec succès.")
        except Error as e:
            print(f"Erreur d'insertion (examen) : {e}")
        finally:
            cursor.close()
            conn.close()

def get_all_examens():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM examen")
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur de lecture (examen) : {e}")
            return []
        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    print("--- Test de la base de données ---")
    conn = get_connection()
    if conn:
        print("Connexion réussie à la base 'monexamen' !")
        conn.close()
    else:
        print("Échec de la connexion.")
