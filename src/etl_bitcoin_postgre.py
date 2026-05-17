import requests
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime
import time

# Loading .env files
load_dotenv()


# Extract bitcoin data
def extract_bitcoin_data():
    url = "https://api.coinbase.com/v2/prices/spot"

    response = requests.get(url)
    data = response.json()

    return data


# Transform bitcoin data
def transform_bitcoin_data(data):
    value = data["data"]["amount"]
    cryptocurrency = data["data"]["base"]
    base_currency = data["data"]["currency"]
    timestamp = datetime.now()

    transformed_data = {
        "value": value,
        "cryptocurrency": cryptocurrency,
        "currency": base_currency,
        "timestamp": timestamp
    }

    return transformed_data


# Create table on database (execute only one once)
def create_table():
    try:
        conn = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port= os.getenv("DB_PORT")
        )
        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS bitcoin_table (
                        id SERIAL PRIMARY KEY,
                        value NUMERIC NOT NULL,
                        cryptocurrency VARCHAR(10) NOT NULL,
                        currency VARCHAR(10) NOT NULL,
                        timestamp TIMESTAMP NOT NULL
                        )
                        """)
            conn.commit()
            print("Table created/verified successfully")
    except Exception as e:
        print(f"Error creating table: {e}")


# Load data on PostgreSQL
def load_bitcoin_postgres(data):
    try:
        conn = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port= os.getenv("DB_PORT")
        )
        with conn.cursor() as cur:
            cur.execute("""
                        INSERT INTO bitcoin_table (value, cryptocurrency, currency, timestamp)
                        VALUES (%s, %s, %s, %s)
            """, (data["value"], data["cryptocurrency"], data["currency"], data["timestamp"])
            )
            conn.commit()
            print("Load successfully")
    except Exception as e:
        print(f"Error load data: {e}")

if __name__ == "__main__":
    # Inicialize create table
    create_table()

    # Main loop
    try:
        while True:
            data = extract_bitcoin_data()
            transformed_data = transform_bitcoin_data(data)
            load_bitcoin_postgres(transformed_data)
            time.sleep(12)
    except KeyboardInterrupt:
        print("Execution was interrupted by the user")