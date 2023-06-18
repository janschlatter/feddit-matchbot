import psycopg2

db_config = {
    "host": "ep-ancient-haze-278884.eu-central-1.aws.neon.tech",
    "port": 5432,
    "dbname": "neondb",
    "user": "matchbot",
    "password": "IduEq7r4aeKD",
    "sslmode": "prefer",
}

try:
    connection = psycopg2.connect(**db_config)
    print("Connected to the PostgreSQL database successfully.")
    connection.close()
except psycopg2.Error as error:
    print(f"Error connecting to the PostgreSQL database: {error}")
