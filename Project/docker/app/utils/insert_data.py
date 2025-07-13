import psycopg2
import csv
import os

# Nom de la table
table_name = "inflation"

# Requête de création de la table
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    country TEXT,
    country_code TEXT,
    year INTEGER,
    inflation FLOAT
);
"""

# Colonnes dans l'ordre
table_columns = ["country", "country_code", "year", "inflation"]

# Requête d'insertion (ignore les conflits)
insert_query = f"""
    INSERT INTO {table_name} ({', '.join(table_columns)})
    VALUES ({', '.join(['%s' for _ in table_columns])})
    ON CONFLICT DO NOTHING;
"""

# Récupération de l'URL de la BDD depuis l'env
DATABASE_URL = os.environ.get('DATABASE_URL')
print(f" Connexion à la base via {DATABASE_URL}")

# Connexion à PostgreSQL
def get_conn():
    return psycopg2.connect(DATABASE_URL)

# Création de la table
def create_table(conn):
    cur = conn.cursor()
    try:
        cur.execute(create_table_query)
        conn.commit()
        print(" Table créée ou déjà existante.")
    except Exception as e:
        print(f" Erreur création table : {e}")
    finally:
        cur.close()

# Insertion des données
def insert_data(conn, input_file_path):
    cursor = conn.cursor()
    with open(input_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Ignorer l'en-tête

        for row in csv_reader:
            # Nettoyer les valeurs vides
            row = [None if val == "" else val for val in row]

            # Convertir types
            row[2] = int(row[2])              # year
            row[3] = float(row[3]) if row[3] else None  # inflation

            cursor.execute(insert_query, row)

        conn.commit()
        print(f" Données insérées depuis {input_file_path}")
    cursor.close()

# Point d'entrée
if __name__ == '__main__':
    conn = get_conn()
    create_table(conn)
    insert_data(conn, "data/inflation_data.csv")
    conn.close()
