import psycopg2
import psycopg2.extras
from clientOut import ClientOut


class ClientReport(ClientOut):
    def __init__(
        self, first_name: str, last_name: str, total_balance: float, id: int = None
    ):
        super().__init__(first_name, last_name, id)
        self.total_balance = total_balance

    def __repr__(self):
        return f"{super().__repr__()}, total balance is : {self.total_balance}"

    @classmethod
    def get_client_report(cls, id):
        conn = super().connect()
        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute(
                        """SELECT c.id, c.first_name , c.last_name,SUM(a.balance) as total_balance 
                            FROM clients as c JOIN accounts as a ON c.id = a.client_id WHERE c.id = %s
                            GROUP BY c.id """,
                        (id,),
                    )
                    client_report = cur.fetchone()
                    if not client_report:
                        return None
                    return ClientReport(**client_report)
                except Exception as e:
                    print("error is : ", e)
        conn.close()
