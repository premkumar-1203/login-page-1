import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="project1",
        user="postgres",
        password="1234"
    )


def ensure_users_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id serial PRIMARY KEY, "
        "username text NOT NULL, "
        "password text NOT NULL"
        ")"
    )
    conn.commit()
    cur.close()
    conn.close()
