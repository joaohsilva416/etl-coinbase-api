# ETL Coinbase API

## About
Extract Bitcoin data using the Coinbase API, transform it, and load it into a database. The goal is to monitor Bitcoin price variation in USD.

## Tech Stack
- **Python**: Main programming language
- **Requests**: Library for HTTP requests
- **psycopg2**: Library to connect a database
- **dotenv**: Library to manage environment variables
- **PostgreSQL**: Database to store the data collected
- **TinyDB**: NoSQL database to store the semi-structured data collected
- **Coinbase API**: Bitcoin price data source

## Environment Set-up
If you want to use the etl_bitcoin_postgre.py, you need to set up your environment correctly. 

**1. Install dependencies:**  
If you don't have Poetry installed, follow the [official documentation](https://python-poetry.org/docs/).

```bash
poetry install
```

**2. Set-up the environment variables**  
Create a `.env` file in the project root and add the following variables:

```
DB_NAME=database_name
DB_USER=username
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port
```

**3. Database**  
Make sure the PostgreSQL database is configured and accessible.

## How to Run
**1. Clone the repository**
```bash
git clone git@github.com:<your-user>/etl-coinbase-api.git
```

**2. Navigate to the project folder**
```bash
cd etl-coinbase-api
```

**3. Run the pipeline**
```bash
# TinyDB pipeline
poetry run python src/etl_bitcoin_tinydb.py

# PostgreSQL pipeline
poetry run python src/etl_bitcoin_postgre.py
```

## Screenshots
![Bitcoin Table](assets/query%20example.png)