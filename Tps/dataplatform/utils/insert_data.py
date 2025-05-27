import psycopg2
import csv
from datetime import datetime
import os
# Database connection parameters



table_name = "premier_league_2021"
# SQL commands
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    MatchDate DATE,              -- Date of the match
    HomeTeam VARCHAR(50),        -- Home team name
    AwayTeam VARCHAR(50),        -- Away team name
    FTHG INTEGER,                -- Full-Time Home Goals
    FTAG INTEGER,                -- Full-Time Away Goals
    FTR CHAR(1),                 -- Full-Time Result (H=Home win, D=Draw, A=Away win)
    HTHG INTEGER,                -- Half-Time Home Goals
    HTAG INTEGER,                -- Half-Time Away Goals
    HTR CHAR(1),                 -- Half-Time Result (H=Home win, D=Draw, A=Away win)
    Referee VARCHAR(50),         -- Match referee name
    HoS INTEGER,                  -- Home Shots
    AwS INTEGER,                  -- Away Shots
    HST INTEGER,                 -- Home Shots on Target
    AST INTEGER,                 -- Away Shots on Target
    HF INTEGER,                  -- Home Fouls
    AF INTEGER,                  -- Away Fouls
    HC INTEGER,                  -- Home Corners
    AC INTEGER,                  -- Away Corners
    HY INTEGER,                  -- Home Yellow Cards
    AY INTEGER,                  -- Away Yellow Cards
    HR INTEGER,                  -- Home Red Cards
    AR INTEGER                   -- Away Red Cards
);
"""

table_columns = [
    "MatchDate", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR",
    "HTHG", "HTAG", "HTR", "Referee", "HoS", "AwS", "HST", "AST",
    "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"
]


insert_query = f"""
    INSERT INTO {table_name} ({', '.join(table_columns)})
    VALUES ({', '.join(['%s' for _ in table_columns])})
    ON CONFLICT DO NOTHING;
"""


DATABASE_URL = os.environ.get('DATABASE_URL')
print(DATABASE_URL)
# Connect to the database and execute queries

def get_conn():
    return psycopg2.connect(DATABASE_URL)


def create_user_table(conn):
    cur = conn.cursor()
    print(f"creating query: {create_table_query}")
    try:
        cur.execute(create_table_query)
        conn.commit()
        print("Table users created successfully or already exists.")
        cur.close()
    except Exception as e:
        print(f"Error: {e}")


def insert_user_data(conn, input_file_path):
    cursor = conn.cursor()
    with open(input_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Skip the header row
        next(csv_reader)

        # Insert each row into the database
        for row in csv_reader:
            formatted_row = list(row)
            formatted_row[0] = datetime.strptime(row[0], "%d/%m/%y").strftime("%Y-%m-%d")
            cursor.execute(insert_query, formatted_row)
        conn.commit()
    cursor.close()
    print(f"Data successfully loaded from {input_file_path} into the users table.")


if __name__ == '__main__':
    conn = get_conn()
    create_user_table(conn)
    insert_user_data(conn, "data/premier-league-2021.csv")