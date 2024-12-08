import psycopg2
import psycopg2.extras


conn = psycopg2.connect(
    dbname="bank-app", user="postgres", password="karim123", host="localhost"
)

with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR);")
conn.close()
