import psycopg2

import psycopg2

def get_db_connection():
    return psycopg2.connect(
        "postgresql://neondb_owner:YOUR_PASSWORD@ep-blue-cloud-aobta3fd-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
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
