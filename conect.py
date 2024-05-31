import psycopg2 as psql

def connect_db(query):
    postgres_db = psql.connect(
        database = "dukon",
        user = "postgres",
        password = "7982",
        host = "localhost",
        port = "5432"
    )
    cursor = postgres_db.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    connect_db("""select * from haridor;""")