import psycopg2
from dotenv import dotenv_values

# Create pg connection and cursor (using environment variables)
def create_pg_conn():
    # Load environment variables
    config = dotenv_values("db/scripts/.env")

    conn_params = {
        "dbname": config["DB_NAME"],
        "user": config["DB_USER"],
        "password": config["DB_PASSWORD"],
        "host": config["DB_HOST"],
        "port": int(config["DB_PORT"])
    }

    conn = psycopg2.connect(**conn_params)
    
    cur = conn.cursor()

    return (conn, cur)