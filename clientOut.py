import psycopg2
import psycopg2.extras
from clientCreate import ClientCreate


class ClientOut(ClientCreate):
    def __init__(self, first_name: str, last_name: str, id: int):
        super().__init__(first_name, last_name)
        self.id = id

    def __repr__(self):
        return f"{super().__repr__()}, id = {self.id}"

    @classmethod
    def get_client_by_id(cls, id):
        conn = cls.connect()
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("""SELECT * FROM  clients WHERE id =%s;""", (id,))
                    client = cur.fetchone()
                    if not client:
                        return None
                    return ClientOut(**client)
                except Exception as e:
                    print("error is : ", e)
        conn.close()
