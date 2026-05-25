# Documentation de la Base de Données `monexamen`

Ce projet contient la structure et les scripts nécessaires pour gérer la base de données MySQL `monexamen`. Il est composé de deux fichiers principaux : un script d'initialisation SQL et un module Python pour interagir avec les données.

## 1. La Base de Données (`monexamen`)
La base de données est conçue pour gérer le flux d'informations autour des étudiants, de leurs évaluations (examens et interrogations), ainsi que des livres. Elle est composée de 4 tables distinctes :

- **`etudiant`** : Stocke les informations des étudiants (nom, prénom, email, promotion, département, mot de passe).
- **`livre`** : Gère une liste simple de livres avec leur identifiant et leur titre.
- **`interrogation`** : Enregistre les interrogations organisées par titre, ciblant une promotion et un département précis.
- **`examen`** : Enregistre les examens organisés par titre, pour une promotion et un département donnés.

## 2. Le Fichier `schema.sql`
Ce fichier est le **script de structure** (Data Definition Language - DDL).
Sa fonction est de configurer la base de données vierge. 

**Ce qu'il fait :**
- Il crée la base de données `monexamen` si elle n'existe pas encore.
- Il sélectionne cette base pour les opérations suivantes.
- Il crée les 4 tables (`etudiant`, `livre`, `interrogation`, `examen`) en définissant précisément les colonnes, les types de données (INT, VARCHAR), et les clés primaires (`id` avec auto-incrémentation).

**Comment l'utiliser :**
Pour initialiser votre base de données dans MySQL, vous pouvez importer ce fichier via votre terminal :
```bash
mysql -u root -p < schema.sql
```

## 3. Le Fichier `db.py`
Ce fichier est le **module d'interaction Python**.
Il sert de pont (ou d'interface) entre votre application Python et la base de données MySQL. Il utilise la bibliothèque `mysql-connector-python`.

**Ce qu'il fait :**
- **Connexion** : La fonction `get_connection()` se charge de se connecter à la base de données avec les identifiants (utilisateur `root`, mot de passe `1234`).
- **Fonctions CRUD (Create & Read)** : Pour chaque table, le fichier propose des fonctions pour **insérer** de nouvelles données et pour **lire** les données existantes.
  - Exemples : `insert_etudiant()`, `get_all_etudiants()`, `insert_livre()`, etc.
- **Sécurité et Gestion des erreurs** : Le script utilise des requêtes paramétrées (avec `%s`) pour éviter les failles de sécurité (injections SQL). Il gère également les ouvertures et fermetures de connexion (`cursor.close()`, `conn.close()`) avec des blocs `try/except/finally`.

**Comment l'utiliser :**
Vous pouvez importer ce fichier dans n'importe quel autre script Python de votre projet pour manipuler la base de données facilement sans avoir à réécrire du SQL :
```python
# Exemple dans un autre fichier de votre projet
from db import insert_livre, get_all_livres

# Ajouter un livre
insert_livre("Apprendre Python")

# Récupérer et afficher les livres
livres = get_all_livres()
print(livres)
```
