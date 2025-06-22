import psycopg2
import csv
from datetime import datetime
import os

# Database connection parameters
table_name = "stock_data"

# SQL commands
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    date DATE,                  -- Date of the record
    open FLOAT,                 -- Opening price
    high FLOAT,                 -- Highest price
    low FLOAT,                  -- Lowest price
    close FLOAT,                -- Closing price
    volume BIGINT,              -- Volume of stocks traded
    Name VARCHAR(50)            -- Stock name
);
"""

table_columns = ["date", "open", "high", "low", "close", "volume", "Name"]

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

def create_table(conn):
    cur = conn.cursor()
    print(f"Creating table with query: {create_table_query}")
    try:
        cur.execute(create_table_query)
        conn.commit()
        print("Table created successfully or already exists.")
        cur.close()
    except Exception as e:
        print(f"Error: {e}")

def insert_data(conn, input_file_path):
    cursor = conn.cursor()
    with open(input_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Skip the header row
        next(csv_reader)

        # Insert each row into the database
        for row in csv_reader:
            formatted_row = list(row)
            formatted_row[0] = datetime.strptime(row[0], "%Y-%m-%d").strftime("%Y-%m-%d")  # Format date

            # Replace empty strings with None (interpreted as NULL in PostgreSQL)
            formatted_row = [None if value == "" else value for value in formatted_row]

            cursor.execute(insert_query, formatted_row)
        conn.commit()
    cursor.close()
    print(f"Data successfully loaded from {input_file_path} into the table.")

if __name__ == '__main__':
    conn = get_conn()
    create_table(conn)
    insert_data(conn, "data/stock-data.csv")