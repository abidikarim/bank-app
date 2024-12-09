import psycopg2
import psycopg2.extras


class ClientCreate:
    def __init__(self, first_name: str, last_name: str):
        assert first_name, "first_name is mandatory"
        assert last_name, "last_name is mandatory"
        assert isinstance(first_name, str), "first_name should be a string"
        assert isinstance(last_name, str), "last_name should be a string"
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def connect():
        conn = psycopg2.connect(
            dbname="bank-app", user="postgres", password="karim123", host="localhost"
        )
        return conn

    def __repr__(self):
        return f"Hello , i'm {self.first_name} {self.last_name} "

    def add_client_in_db(self):
        conn = self.connect()
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute(
                        """INSERT INTO clients (first_name, last_name) VALUES(%s, %s)""",
                        (self.first_name, self.last_name),
                    )
                except Exception as e:
                    print(e)
